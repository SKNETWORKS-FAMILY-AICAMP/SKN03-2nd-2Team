<script setup></script>
<template>
  <div class="overflow-hidden rounded-lg bg-gray-700 shadow">
    <div class="text-moonYellow text-4xl font-bold px-4 pt-9 sm:px-6">
      #{{ $attrs.idx }} {{ $attrs.values.movie_name }}
    </div>
    <div class="bg-gray-700 px-4 py-5 sm:p-6">
      <div class="mx-auto max-w-7xl">
        <div class="grid grid-cols-1 gap-px sm:grid-cols-2">
          <div class="bg-gray-700 mb-4">
            <p class="text-sm font-medium leading-6 text-gray-400">장르</p>
            <p class="mt-2 flex items-baseline gap-x-2">
              <span class="text-2xl font-semibold tracking-tight text-white">
                {{ $attrs.values.genre }}
              </span>
            </p>
          </div>
          <div class="bg-gray-700 mb-4">
            <p class="text-sm font-medium leading-6 text-gray-400">개봉일</p>
            <p class="mt-2 flex items-baseline gap-x-2">
              <span class="text-2xl font-semibold tracking-tight text-white">
                {{ $attrs.values.open_date }}
              </span>
            </p>
          </div>
          <div class="bg-gray-700 mb-4">
            <p class="text-sm font-medium leading-6 text-gray-400">누적 관객수</p>
            <p class="mt-2 flex items-baseline gap-x-2">
              <span class="text-2xl font-semibold tracking-tight text-white">
                {{ $attrs.values.audience }}
              </span>
            </p>
          </div>
          <div class="bg-gray-700 mb-4">
            <p class="text-sm font-medium leading-6 text-gray-400">누적 매출액</p>
            <p class="mt-2 flex items-baseline gap-x-2">
              <span class="text-2xl font-semibold tracking-tight text-white">
                {{ $attrs.values.sales }}
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
