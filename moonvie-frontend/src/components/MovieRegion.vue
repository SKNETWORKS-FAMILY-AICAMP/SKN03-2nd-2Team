<script setup>
import { onMounted, ref } from 'vue'
import {
  Listbox,
  ListboxButton,
  ListboxLabel,
  ListboxOption,
  ListboxOptions
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
import * as movieApi from '@/api/movie'
import { useTopMovieStore } from '@/stores/topMovieStore'
import { storeToRefs } from 'pinia'

const topMovieStore = useTopMovieStore()
const { topMovies } = storeToRefs(topMovieStore)

const getRegion = (req) => {
  movieApi
    .getRegionMovies(req)
    .then((res) => {
      topMovies.value = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}
const regions = [
  { id: 0, name: '전국' },
  { id: 1, name: '서울시' },
  { id: 2, name: '경기도' },
  { id: 3, name: '강원도' },
  { id: 4, name: '충청북도' },
  { id: 5, name: '충청남도' },
  { id: 6, name: '경상북도' },
  { id: 7, name: '경상남도' },
  { id: 8, name: '전라북도' },
  { id: 9, name: '전라남도' },
  { id: 10, name: '제주도' },
  { id: 11, name: '부산시' },
  { id: 12, name: '대구시' },
  { id: 13, name: '대전시' },
  { id: 14, name: '울산시' },
  { id: 15, name: '인천시' },
  { id: 16, name: '광주시' },
  { id: 17, name: '세종시' }
]

const selected = ref(regions[0])

const fetchRegionMovies = () => {
  getRegion(selected.value.id)
}
onMounted(() => {
  fetchRegionMovies()
})
</script>

<template>
  <div class="mx-auto py-4 mb-8 pb-4 border-b-2 border-white/10">
    <Listbox as="div" v-model="selected" class="w-64">
      <ListboxLabel class="block text-sm font-medium leading-6">지역 선택</ListboxLabel>
      <div class="relative mt-2">
        <ListboxButton
          class="relative w-full cursor-default rounded-md bg-white py-1.5 pl-3 pr-10 text-left text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:outline-none focus:ring-2 focus:ring-moonYellow/10 sm:text-sm sm:leading-6"
        >
          <span class="block truncate">{{ selected.name }}</span>
          <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
            <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
          </span>
        </ListboxButton>

        <transition
          leave-active-class="transition ease-in duration-100"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <ListboxOptions
            class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm"
          >
            <ListboxOption
              as="template"
              v-for="region in regions"
              :key="region.id"
              :value="region"
              v-slot="{ active, selected }"
              @click="fetchRegionMovies"
            >
              <li
                :class="[
                  active ? 'bg-moonYellow/70 text-gray-900' : 'text-gray-900',
                  'relative cursor-default select-none py-2 pl-3 pr-9'
                ]"
              >
                <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">{{
                  region.name
                }}</span>

                <span
                  v-if="selected"
                  :class="[
                    active ? 'text-white' : 'text-moonYellow/70',
                    'absolute inset-y-0 right-0 flex items-center pr-4'
                  ]"
                >
                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                </span>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
</template>
