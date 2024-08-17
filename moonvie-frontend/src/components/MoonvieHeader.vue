<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">
        <img src="@/assets/logo.png" alt="Moonvie Logo" height="30" />
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-start" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/" class="nav-link" style="font-weight: bold" @click.prevent
              >홈</router-link
            >
          </li>
          <li class="nav-item dropdown">
            <router-link
              to="/season"
              class="nav-link dropdown-toggle"
              style="font-weight: bold"
              id="seasonDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              @click.prevent
              >시즌별</router-link
            >
            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="seasonDropdown">
              <li>
                <router-link to="/season" class="dropdown-item" @click="setViewMode('table')"
                  >표</router-link
                >
              </li>
              <li>
                <router-link to="/season" class="dropdown-item" @click="setViewMode('chart')"
                  >차트</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <router-link
              to="/period"
              class="nav-link dropdown-toggle"
              style="font-weight: bold"
              id="periodDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              @click.prevent
              >기간별</router-link
            >
            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="periodDropdown">
              <li>
                <router-link to="/period" class="dropdown-item" @click="setViewMode('table')"
                  >표</router-link
                >
              </li>
              <li>
                <router-link to="/period" class="dropdown-item" @click="setViewMode('chart')"
                  >차트</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <router-link
              to="/genre"
              class="nav-link dropdown-toggle"
              style="font-weight: bold"
              id="genreDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              @click.prevent
              >장르별</router-link
            >
            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="genreDropdown">
              <li>
                <router-link to="/genre" class="dropdown-item" @click="setViewMode('table')"
                  >표</router-link
                >
              </li>
              <li>
                <router-link to="/genre" class="dropdown-item" @click="setViewMode('chart')"
                  >차트</router-link
                >
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const setViewMode = (mode) => {
  store.viewMode = mode
}
</script>

<style scoped>
.navbar-nav .dropdown:hover > .dropdown-menu {
  display: block;
  transition: all 0.3s ease-in-out;
  opacity: 1;
  visibility: visible;
  max-height: 200px; /* Adjust as needed */
}

.dropdown-menu {
  display: block;
  opacity: 0;
  visibility: hidden;
  max-height: 0;
  overflow: hidden;
  transition: all 0.3s ease-in-out;
}

.navbar-nav .dropdown:hover > .dropdown-menu {
  opacity: 1;
  visibility: visible;
  max-height: 200px; /* Adjust as needed */
}
</style>
