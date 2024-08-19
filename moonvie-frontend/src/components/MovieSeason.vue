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

const getSeason = (req) => {
  movieApi
    .getSeasonMovies(req)
    .then((res) => {
      topMovies.value = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}

const seasons = [
  { id: 0, name: '봄' },
  { id: 1, name: '여름' },
  { id: 2, name: '가을' },
  { id: 3, name: '겨울' },
  { id: 4, name: '명절' },
  { id: 5, name: '가정의 달(5월)' },
  { id: 6, name: '크리마스 시즌(12월 말)' }
]

const selected = ref(seasons[0])

const fetchSeasonMovies = () => {
  getSeason(selected.value.id)
}
onMounted(() => {
  fetchSeasonMovies()
})
</script>

<template>
  <div class="mx-auto py-4 mb-8 pb-4 border-b-2 border-white/10">
    <Listbox as="div" v-model="selected" class="w-64">
      <ListboxLabel class="block text-sm font-medium leading-6">시즌 선택</ListboxLabel>
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
              v-for="season in seasons"
              :key="season.id"
              :value="season"
              v-slot="{ active, selected }"
              @click="fetchSeasonMovies"
            >
              <li
                :class="[
                  active ? 'bg-moonYellow/70 text-gray-900' : 'text-gray-900',
                  'relative cursor-default select-none py-2 pl-3 pr-9'
                ]"
              >
                <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">{{
                  season.name
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
