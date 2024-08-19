import { http } from '@/api/axios'

export async function getTopMovies(startDate, endDate) {
  return await http.get(`/top?startdate=${startDate}&enddate=${endDate}}`)
}
export async function getSeasonMovies(req) {
  return await http.get(`/season/${req}`)
}
export async function getRegionMovies(req) {
  return await http.get(`/region/${req}`)
}
