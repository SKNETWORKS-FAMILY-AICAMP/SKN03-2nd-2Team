<template>
	<div class="container mt-5">
		<h1 class="text-center">Weekly Box Office Data</h1>
		<div class="row mb-3">
			<div class="col-md-6">
				<label for="start-date" class="form-label">Start Date:</label>
				<input type="date" id="start-date" v-model="startDate" class="form-control">
			</div>
			<div class="col-md-6">
				<label for="end-date" class="form-label">End Date:</label>
				<input type="date" id="end-date" v-model="endDate" class="form-control">
			</div>
		</div>
		<div class="row mb-3">
			<div class="col-md-6">
				<button @click="filterData" class="btn btn-primary w-100">검색</button>
			</div>
			<div class="col-md-6">
				<button @click="resetData" class="btn btn-secondary w-100">초기화</button>
			</div>
		</div>
		<div class="mb-3">
			<h2>출력할 열 선택</h2>
			<div class="dropdown">
				<button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
					열 선택
				</button>
				<div class="dropdown-menu dropdown-menu-grid p-3" aria-labelledby="dropdownMenuButton">
					<div class="row">
						<div v-for="header in headers" :key="header" class="col-6 col-md-4 dropdown-item">
							<input type="checkbox" :id="header" :value="header" v-model="selectedColumns" class="form-check-input me-2">
							<label :for="header" class="form-check-label">{{ header }}</label>
						</div>
					</div>
				</div>
			</div>
		</div>
		<table v-if="isSearched" class="table table-striped table-bordered">
			<thead>
				<tr>
					<th v-for="header in selectedColumns" :key="header">{{ header }}</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="row in sortedFilteredData" :key="row.id">
					<td v-for="header in selectedColumns" :key="header">{{ row[header] }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	import csvData from '@/components/WeeklyBoxOffice/0_WeeklyBoxOfficeData.csv';
	export default {
		data() {
			return {
				headers: [],
				rawData: [],
				filteredData: [],
				startDate: '',
				endDate: '',
				selectedColumns: ['movieNm', 'openDt', 'audiAcc', 'showRange'],
				isSearched: false // 검색 여부를 나타내는 상태 추가
			};
		},
		mounted() {
			this.initializeData();
		},
		computed: {
			sortedFilteredData() {
				return this.filteredData.slice().sort((a, b) => b.audiAcc - a.audiAcc);
			}
		},
		methods: {
			initializeData() {
				if (csvData.length > 1) {
					this.headers = csvData[0];
					this.rawData = csvData.slice(1).map(row => {
						const rowData = {};
						this.headers.forEach((header, index) => {
							rowData[header] = row[index];
						});
						return rowData;
					});
					this.filteredData = this.rawData;
				}
			},
			filterData() {
				let filtered = this.rawData;

				// 1. 기간에 맞춰 데이터 필터링
				if (this.startDate && this.endDate) {
					filtered = filtered.filter(row => {
						const openDate = new Date(row.openDt);
						const startDate = new Date(this.startDate);
						const endDate = new Date(this.endDate);
						return openDate >= startDate && openDate <= endDate;
					});
				}

				// 2. MovieNm을 기준으로 오름차순 정렬하고, 중복된 MovieNm 중 audiAcc가 더 큰 항목만 남기기
				filtered.sort((a, b) => a.movieNm.localeCompare(b.movieNm));
				const uniqueMovies = {};
				filtered.forEach(row => {
					const movieName = row.movieNm;
					if (!uniqueMovies[movieName] || row.audiAcc > uniqueMovies[movieName].audiAcc) {
						uniqueMovies[movieName] = row;
					}
				});

				// 3. MovieNm 기준으로 정렬된 데이터를 audiAcc 기준으로 내림차순 정렬
				this.filteredData = Object.values(uniqueMovies).sort((a, b) => b.audiAcc - a.audiAcc);

				// 검색이 수행되었음을 표시
				this.isSearched = true;
			},
			resetData() {
				this.startDate = '';
				this.endDate = '';
				this.filteredData = this.rawData;
				this.isSearched = false; // 초기화 시 검색 상태도 초기화
			}
		}
	};
</script>