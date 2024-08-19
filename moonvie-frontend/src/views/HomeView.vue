<script setup>
const people = [
  {
    name: '문희선',
    role: 'PM / Backend',
    imageUrl: '/src/assets/members/heesun.png'
  },
  {
    name: '박중헌',
    role: 'FullStack / Data Analyst',
    imageUrl: '/src/assets/members/joongheon.png'
  },
  {
    name: '김재성',
    role: 'Data Analyst',
    imageUrl: '/src/assets/members/jaesung.png'
  },
  {
    name: '송영빈',
    role: 'Frontend',
    imageUrl: '/src/assets/members/youngbin.png'
  },
  {
    name: '진윤화',
    role: 'Frontend',
    imageUrl: '/src/assets/members/yunhwa.png'
  }
]
</script>
<template>
  <div class="relative isolate overflow-hidden !p-0">
    <svg
      class="absolute inset-0 -z-10 h-full w-full stroke-white/10 [mask-image:radial-gradient(100%_100%_at_top_right,white,transparent)]"
      aria-hidden="true"
    >
      <defs>
        <pattern
          id="983e3e4c-de6d-4c3f-8d64-b9761d1534cc"
          width="200"
          height="200"
          x="50%"
          y="-1"
          patternUnits="userSpaceOnUse"
        >
          <path d="M.5 200V.5H200" fill="none" />
        </pattern>
      </defs>
      <svg x="50%" y="-1" class="overflow-visible fill-gray-800/20">
        <path
          d="M-200 0h201v201h-201Z M600 0h201v201h-201Z M-400 600h201v201h-201Z M200 800h201v201h-201Z"
          stroke-width="0"
        />
      </svg>
      <rect
        width="100%"
        height="100%"
        stroke-width="0"
        fill="url(#983e3e4c-de6d-4c3f-8d64-b9761d1534cc)"
      />
    </svg>
    <div
      class="absolute left-[calc(50%-4rem)] top-10 -z-10 transform-gpu blur-3xl sm:left-[calc(50%-18rem)] lg:left-48 lg:top-[calc(50%-30rem)] xl:left-[calc(50%-24rem)]"
      aria-hidden="true"
    >
      <div
        class="aspect-[1108/632] w-[69.25rem] bg-gradient-to-r from-[#80caff] to-[#4f46e5] opacity-20"
        style="
          clip-path: polygon(
            73.6% 51.7%,
            91.7% 11.8%,
            100% 46.4%,
            97.4% 82.2%,
            92.5% 84.9%,
            75.7% 64%,
            55.3% 47.5%,
            46.5% 49.4%,
            45% 62.9%,
            50.3% 87.2%,
            21.3% 64.1%,
            0.1% 100%,
            5.4% 51.1%,
            21.4% 63.9%,
            58.9% 0.2%,
            73.6% 51.7%
          );
        "
      />
    </div>
    <div
      class="absolute left-[calc(50%-4rem)] top-10 -z-10 transform-gpu blur-3xl sm:left-[calc(50%-18rem)] lg:left-48 lg:top-[calc(50%-30rem)] xl:left-[calc(50%-24rem)]"
      aria-hidden="true"
    ></div>
    <div class="mx-auto max-w-7xl px-6 pb-24 pt-10 sm:pb-32 lg:flex lg:px-8 lg:py-40">
      <div class="mx-auto max-w-2xl flex-shrink-0 lg:mx-0 lg:max-w-xl lg:pt-8">
        <img class="h-11" src="@/assets/logo.png" alt="Your Company" />
        <h1 class="mt-10 text-4xl font-bold tracking-tight text-moonYellow sm:text-6xl">
          Movie Insights
        </h1>
        <p class="mt-6 text-lg leading-8 text-gray-300">
          코로나19 팬데믹은 영화 산업에 상당한 변화를 가져왔습니다. 팬데믹 이전에는 영화관에서의
          관람이 주요 소비 방식이었으나, 팬데믹 동안 많은 영화관이 문을 닫고 사람들은 집에서
          콘텐츠를 소비하는 방식으로 전환되었습니다. 그러나 여전히 상업적으로 살아남는 영화는
          존재합니다. 문비(Moonvie)는 코로나19 팬데믹 이전 이후 상업적으로 성공한 영화에 대한
          데이터를 분석함으로써, 영화 제작자들이 팬데믹 이후 변화된 환경에서 경쟁력을 갖출 수 있도록
          인사이트를 제공하고자 합니다.
        </p>
        <div class="mt-10 flex items-center gap-x-6">
          <a
            href="/top"
            class="rounded-md bg-moonYellow/30 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-moonYellow/70 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-moonYellow"
            >Watch Top Movies</a
          >
          <a href="/cloud" class="text-sm font-semibold leading-6 text-white"
            >Show Movie Cloud <span aria-hidden="true">→</span></a
          >
        </div>
      </div>
      <div
        class="mx-auto mt-16 flex max-w-2xl sm:mt-24 lg:ml-10 lg:mr-0 lg:mt-0 lg:max-w-none lg:flex-none xl:ml-32"
      >
        <div class="max-w-3xl flex-none sm:max-w-5xl lg:max-w-none">
          <img
            src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png"
            alt="App screenshot"
            width="2432"
            height="1442"
            class="w-[76rem] rounded-md bg-white/5 shadow-2xl ring-1 ring-white/10"
          />
        </div>
      </div>
    </div>
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <h2 class="text-3xl font-bold tracking-tight text-moonYellow sm:text-4xl">
          Team. 세일러 문과 데스 버스터즈
        </h2>
        <p class="mt-6 leading-8 text-gray-300">
          나, 문희선. 조금 얼빠지고 울보인 보통 여자아이였는데, 우연히 악당(박중헌)을 만나서 정의의
          아군 세일러 문이 되어버렸어. 대망의 미소녀와 악당 데스 버스터즈가 선보이는 쾌감 액션 영화
          프로젝트 드디어 등장!!
        </p>
      </div>
      <ul
        role="list"
        class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-14 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 xl:grid-cols-4"
      >
        <li v-for="person in people" :key="person.name">
          <img
            class="aspect-[14/13] w-full rounded-2xl object-cover"
            :src="person.imageUrl"
            alt=""
          />
          <h3 class="mt-6 text-lg font-semibold leading-8 tracking-tight text-white">
            {{ person.name }}
          </h3>
          <p class="text-base leading-7 text-gray-300">{{ person.role }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>
