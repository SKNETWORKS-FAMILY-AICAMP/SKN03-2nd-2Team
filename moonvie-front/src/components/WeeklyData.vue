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
				startDate: '1970-01-01', // Start Date 디폴트 값 설정
				endDate: new Date().toISOString().substr(0, 10), // End Date 디폴트 값 설정
				selectedColumns: ['movieNm', 'openDt', 'audiAcc', 'showRange'],
				isSearched: false // 검색 여부를 나타내는 상태 추가
			};
		},
		mounted() {
			this.initializeData();
		},
		computed: {
			sortedFilteredData() {
				return this.getSortedFilteredData();
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
				this.isSearched = true;
				this.filteredData = this.getFilteredData();
			},
			resetData() {
				this.startDate = '1970-01-01';
				this.endDate = new Date().toISOString().substr(0, 10);
				this.filteredData = this.rawData;
				this.isSearched = false; // 초기화 시 검색 상태도 초기화
			},
			getFilteredData() {
				let filtered = this.rawData;

				// 1. 기간에 맞춰 데이터 필터링
				if (this.startDate && this.endDate) {
					const startDate = new Date(this.startDate);
					const endDate = new Date(this.endDate);
					filtered = filtered.filter(row => {
						const openDate = new Date(row.openDt);
						return openDate >= startDate && openDate <= endDate;
					});
				}

				// 2. MovieNm을 기준으로 오름차순 정렬하고, 중복된 MovieNm 중 audiAcc가 더 큰 항목만 남기기
				const uniqueMovies = filtered
					.sort((a, b) => a.movieNm.localeCompare(b.movieNm))
					.reduce((acc, row) => {
						if (!acc[row.movieNm] || row.audiAcc > acc[row.movieNm].audiAcc) {
							acc[row.movieNm] = row;
						}
						return acc;
					}, {});

				// 3. MovieNm 기준으로 정렬된 데이터를 audiAcc 기준으로 내림차순 정렬
				return Object.values(uniqueMovies).sort((a, b) => b.audiAcc - a.audiAcc);
			},
			getSortedFilteredData() {
				return this.filteredData.sort((a, b) => b.audiAcc - a.audiAcc);
			}
		}
	};
</script>

<style scoped>
.container {
	max-width: 800px;
	margin: 0 auto;
	padding: 20px;
	font-family: Arial, sans-serif;
}

h1 {
	text-align: center;
	color: #333;
}

.date-filters {
	display: flex;
	justify-content: space-between;
	margin-bottom: 20px;
}

.date-filters label {
	margin-right: 10px;
}

.date-filters input {
	margin-right: 20px;
}

.column-selection {
	margin-bottom: 20px;
}

.checkbox-container {
	display: inline-block;
	margin-right: 10px;
}

.styled-table {
	width: 100%;
	border-collapse: collapse;
	margin: 25px 0;
	font-size: 18px;
	text-align: left;
}

.styled-table th, .styled-table td {
	padding: 12px 15px;
}

.styled-table thead tr {
	background-color: #009879;
	color: #ffffff;
	text-align: left;
}

.styled-table tbody tr {
	border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
	background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
	border-bottom: 2px solid #009879;
}

.dropdown-menu-grid {
	width: 100%; /* 드롭다운 메뉴를 화면 너비에 맞게 조정 */
}

.dropdown-menu-grid .row {
	display: flex;
	flex-wrap: wrap;
}

.dropdown-menu-grid .col-6 {
	flex: 0 0 50%;
	max-width: 50%;
}

.dropdown-menu-grid .col-md-4 {
	flex: 0 0 33.3333%;
	max-width: 33.3333%;
}
</style>
