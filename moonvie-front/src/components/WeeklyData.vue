<template>
	<div class="container">
		<h1>Weekly Box Office Data</h1>
		<div class="date-filters">
			<label for="start-date">Start Date:</label>
			<input type="date" id="start-date" v-model="startDate">
			<label for="end-date">End Date:</label>
			<input type="date" id="end-date" v-model="endDate">
			<button @click="filterData">검색</button>
			<button @click="resetData">초기화</button>
		</div>
		<div class="column-selection">
			<h2>출력할 열 선택</h2>
			<div v-for="header in headers" :key="header" class="checkbox-container">
				<input type="checkbox" :id="header" :value="header" v-model="selectedColumns">
				<label :for="header">{{ header }}</label>
			</div>
		</div>
		<table class="styled-table">
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
				selectedColumns: ['movieNm', 'openDt', 'audiAcc'] // 기본적으로 movieNm, audiAcc, openDt가 선택됨
			};
		},
		mounted() {
			this.initializeData();
		},
		computed: {
			sortedFilteredData() {
				return this.filteredData.slice().sort((a, b) => b.audiCnt - a.audiCnt);
			}
		},
		methods: {
			initializeData() {
				if (csvData.length > 1) {
					// 첫 번째 행을 헤더로 사용하고 나머지 데이터를 초기화
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
				if (this.startDate && this.endDate) {
					this.filteredData = this.rawData.filter(row => {
						const openDate = new Date(row.openDt);
						const startDate = new Date(this.startDate);
						const endDate = new Date(this.endDate);
						return openDate >= startDate && openDate <= endDate;
					});
				} else {
					this.filteredData = this.rawData;
				}
			},
			resetData() {
				this.startDate = '';
				this.endDate = '';
				this.filteredData = this.rawData;
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
</style>
