import { http } from '@/api/axios'

export async function getMoneyCovid() {
  return await http.get('/covid/money')
}
export async function getPeopleCovid() {
  return await http.get('/covid/people')
}
