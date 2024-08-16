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
            <router-link to="/" class="nav-link" style="font-weight: bold">홈</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/month" class="nav-link" style="font-weight: bold"
              >월/분기별</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/period" class="nav-link" style="font-weight: bold"
              >기간별</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/genre" class="nav-link" style="font-weight: bold">장르별</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup></script>

<style scoped></style>
