/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        moonYellow: '#FFC77D' // 여기에 사용자 정의 색상 추가
      }
    }
  },
  plugins: []
}
