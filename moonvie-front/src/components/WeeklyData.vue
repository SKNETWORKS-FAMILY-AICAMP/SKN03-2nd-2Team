<template>
	<div>
		<h1>Weekly Box Office Data</h1>
		<label for="start-date">Start Date:</label>
		<input type="date" id="start-date" v-model="startDate" @change="filterData">
		<label for="end-date">End Date:</label>
		<input type="date" id="end-date" v-model="endDate" @change="filterData">
		<table>
			<thead>
				<tr>
					<th v-for="header in headers" :key="header">{{ header }}</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="row in filteredData" :key="row.id">
					<td v-for="(value, key) in row" :key="key">{{ value }}</td>
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
				rawData: csvData,
				filteredData: csvData,
				startDate: '',
				endDate: ''
			};
		},
		mounted() {
			this.initializeData();
		},
		methods: {
			initializeData() {
				if (this.rawData.length > 0) {
					this.headers = Object.keys(this.rawData[0]);
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
			}
		}
	};
</script>
