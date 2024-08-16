<template>
  <header class="masthead text-center text-white">
    <div class="masthead-content">
      <div class="container px-5">
        <h1 class="masthead-heading mb-4">세일러 문과 데스 버스터즈</h1>
        <p class="masthead-subheading mb-0">
          코로나19 팬데믹은 영화 산업에 상당한 변화를 가져왔습니다. 팬데믹 이전에는 영화관에서의
          관람이 주요 소비 방식이었으나, 팬데믹 동안 많은 영화관이 문을 닫고 사람들은 집에서
          콘텐츠를 소비하는 방식으로 전환되었습니다. 그러나 여전히 상업적으로 살아남는 영화는
          존재합니다. 코로나19 팬데믹 이전 이후 상업적으로 성공한 영화에 대한 데이터를 분석함으로써,
          영화 제작자들이 팬데믹 이후 변화된 환경에서 경쟁력을 갖출 수 있도록 인사이트를 제공하고자
          합니다.
        </p>
        <a href="#members" class="arrow-down">
          <i class="fas fa-chevron-down"></i>
        </a>
      </div>
    </div>
    <div class="bg-circle-1 bg-circle"></div>
    <div class="bg-circle-2 bg-circle"></div>
    <div class="bg-circle-3 bg-circle"></div>
    <div class="bg-circle-4 bg-circle"></div>
  </header>
  <div id="members" class="container text-center text-white mt-5 members-section">
    <h1 class="masthead-heading mb-5 mt-5">members</h1>
    <div class="row">
      <div class="col-md-4 mb-4" v-for="member in members" :key="member.name">
        <div class="member-card">
          <img :src="member.image" :alt="member.name" class="img-fluid rounded-circle mb-2" />
          <h3>{{ member.name }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, onMounted } from 'vue'
import kimjaesung from '@/assets/members/kimjaesung.png'
import moonheesun from '@/assets/members/moonheesun.png'
import cassandra from '@/assets/members/cassandra.png'
import songyoungbin from '@/assets/members/songyoungbin.png'
import jinyunhwa from '@/assets/members/jinyunhwa.png'

const members = reactive([
  { name: '김재성', image: kimjaesung },
  { name: '문희선', image: moonheesun },
  { name: '박중헌', image: cassandra },
  { name: '송영빈', image: songyoungbin },
  { name: '진윤화', image: jinyunhwa }
])

onMounted(() => {
  const membersSection = document.getElementById('members')
  window.addEventListener('scroll', () => {
    const sectionTop = membersSection.getBoundingClientRect().top
    const windowHeight = window.innerHeight
    if (sectionTop < windowHeight) {
      membersSection.classList.add('visible')
    }
  })
})
</script>

<style scoped>
.masthead {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 30rem;
  padding-top: 8rem;
  padding-bottom: 8rem;
  background: linear-gradient(to right, #ff7e5f, #feb47b);
}
.masthead-content {
  position: relative;
  z-index: 2;
}
.masthead-heading {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 2rem; /* 간격 추가 */
}
.masthead-subheading {
  font-size: 1.25rem;
  font-weight: 300;
}
.arrow-down {
  display: inline-block;
  margin-top: 2rem;
  font-size: 2rem;
  color: white;
  animation: bounce 2s infinite;
}
@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}
.bg-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
}
.bg-circle-1 {
  width: 15rem;
  height: 15rem;
  top: 2rem;
  right: 2rem;
}
.bg-circle-2 {
  width: 10rem;
  height: 10rem;
  bottom: 2rem;
  right: 2rem;
}
.bg-circle-3 {
  width: 20rem;
  height: 20rem;
  bottom: 2rem;
  left: 2rem;
}
.bg-circle-4 {
  width: 10rem;
  height: 10rem;
  top: 2rem;
  left: 2rem;
}
.members-section {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}
.members-section.visible {
  opacity: 1;
}
.member-heading {
  font-size: 2.5rem;
  font-weight: 700;
  color: #333;
}
.member-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  transition: transform 0.3s;
}
.member-card:hover {
  transform: scale(1.05);
}
.img-fluid {
  width: 150px;
  height: 150px;
  object-fit: cover;
}
.rounded-circle {
  border-radius: 50%;
}
.mb-2 {
  margin-bottom: 0.5rem;
}
.mb-4 {
  margin-bottom: 2rem;
}
</style>
