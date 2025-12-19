<template>
  <div>
    <div style="padding: 12px; text-align: center">
      <button @click="$router.push('/create')">下单</button>
      <button @click="$router.push('/nearby')" style="margin-left: 12px">
        接单
      </button>
    </div>

    <!-- 路由出口：页面变化就在这里发生 -->
    <router-view />
  </div>
</template>
