<template>
  <header class="masthead text-center text-white">
    <div class="masthead-content d-flex align-items-center justify-content-center">
      <div class="container px-5 text-center">
        <h1 class="masthead-heading mb-4"><i class="fas fa-moon"></i> Sailor Moon</h1>
        <h1 class="masthead-heading mb-4"><i class="fas fa-star"></i> and</h1>
        <h1 class="masthead-heading mb-4"><i class="fas fa-skull-crossbones"></i> Death Busters</h1>
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
  background: linear-gradient(to right, #03346e, #6eacda);
}
.masthead-content {
  position: relative;
  z-index: 2;
  height: 100%; /* 화면 전체 높이 */
  display: flex;
  align-items: center; /* 수직 정가운데 배치 */
  justify-content: center; /* 수평 정가운데 배치 */
}
.container {
  width: 100%; /* 가로로 꽉 채움 */
  text-align: center; /* 텍스트 정가운데 배치 */
}
.masthead-heading {
  font-size: 4.5rem;
  font-weight: 1000;
  margin-bottom: 2rem; /* 간격 추가 */
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
