<template>
  <div class="container text-center text-white mt-5">
    <h1 class="bold-text">세일러 문과 데스 버스터즈</h1>
    <p>코로나19 팬데믹은 영화 산업에 상당한 변화를 가져왔습니다. 팬데믹 이전에는 영화관에서의 관람이 주요 소비 방식이었으나, 팬데믹 동안 많은 영화관이 문을 닫고 사람들은 집에서 콘텐츠를 소비하는 방식으로 전환되었습니다. 그러나 여전히 상업적으로 살아남는 영화는 존재합니다. 코로나19 팬데믹 이전 이후 상업적으로 성공한 영화에 대한 데이터를 분석함으로써, 영화 제작자들이 팬데믹 이후 변화된 환경에서 경쟁력을 갖출 수 있도록 인사이트를 제공하고자 합니다.</p>
    <h1 class="bold-text">member</h1>
    <div class="row">
      <div class="col-md-4" v-for="member in members" :key="member.name">
        <img :src="require(`@/assets/members/${member.image}`)" alt="member.name" class="img-fluid rounded-circle mb-2">
        <h3>{{ member.name }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MoonvieHome',
  data() {
    return {
      members: [
        { name: '김재성', image: 'kimjaesung.png' },
        { name: '문희선', image: 'moonheesun.png' },
        { name: '박중헌', image: 'cassandra.png' },
        { name: '송영빈', image: 'songyoungbin.png' },
        { name: '진윤화', image: 'jinyunhwa.png' },
      ]
    };
  }
};
</script>

<style scoped>
.bold-text {
  font-weight: bold;
}
.container {
  flex: 1;
}
.img-fluid {
  max-width: 100%;
  height: auto;
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
</style>
