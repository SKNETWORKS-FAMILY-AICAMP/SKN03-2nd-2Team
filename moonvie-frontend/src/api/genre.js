import { http } from '@/api/axios'

export async function getSeasonGenre() {
  return await http.get('/genre/season')
}
export async function getHolidayGenre() {
  return await http.get('/genre/holiday')
}
export async function getCovidGenre() {
  return await http.get('/genre/covid')
}
