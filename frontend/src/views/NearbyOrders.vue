<template>
  <div class="container">
    <h2>附近可接订单</h2>

    <!-- 地图 -->
    <div id="map" class="map">
      <div v-if="!mapReady" class="map-placeholder">
        地图加载中…
      </div>
    </div>

    <button @click="loadOrders">刷新附近订单</button>

    <ul v-if="orders.length">
      <li v-for="item in orders" :key="item.order_id">
        <p><strong>描述：</strong>{{ item.desc }}</p>
        <p><strong>距离：</strong>{{ item.distance }} 米</p>

        <button @click="acceptOrder(item.order_id)">
          接单
        </button>

        <button @click="planRoute(item)">
          查看路线
        </button>
      </li>
    </ul>

    <p v-else>暂无附近订单</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import request from "../api/request";

/* ========================
 * 状态
 * ======================== */
const orders = ref([]);
const mapReady = ref(false);
let map = null;
let markers = [];
let driving = null;

/* ========================
 * 模拟服务者信息
 * ======================== */
const providerId = 1;

const currentLocation = {
  lat: 39.9165,
  lng: 116.4320,
};

/* ========================
 * 初始化地图
 * ======================== */
const initMap = () => {
  if (!window.AMap || !window.AMap.Map) return;

  map = new AMap.Map("map", {
    zoom: 14,
    center: [currentLocation.lng, currentLocation.lat],
  });

  // 我的当前位置
  new AMap.Marker({
    position: [currentLocation.lng, currentLocation.lat],
    map,
    title: "我的位置",
  });

  // 初始化驾车路线服务
  driving = new AMap.Driving({
    map,
    policy: AMap.DrivingPolicy.LEAST_TIME,
  });

  mapReady.value = true;
};

/* ========================
 * 加载附近订单
 * ======================== */
const loadOrders = async () => {
  const res = await request.get("/order/nearby", {
    params: {
      lat: currentLocation.lat,
      lng: currentLocation.lng,
      radius: 2000,
    },
  });

  orders.value = res.data.orders || [];

  if (!map) return;

  markers.forEach((m) => m.setMap(null));
  markers = [];

  orders.value.forEach((item) => {
    const marker = new AMap.Marker({
      position: [item.lng, item.lat],
      map,
      title: item.desc,
    });

    marker.on("click", () => {
      planRoute(item);
    });

    markers.push(marker);
  });
};

/* ========================
 * 路线规划（核心加分点）
 * ======================== */
const planRoute = (order) => {
  if (!driving) return;

  driving.clear();

  driving.search(
    new AMap.LngLat(currentLocation.lng, currentLocation.lat),
    new AMap.LngLat(order.lng, order.lat),
    (status, result) => {
      if (status === "complete") {
        console.log("路线规划成功");
      } else {
        console.error("路线规划失败", result);
      }
    }
  );
};

/* ========================
 * 接单
 * ======================== */
const acceptOrder = async (orderId) => {
  await request.post("/order/accept", {
    orderId,
    providerId,
  });

  alert("接单成功");
  loadOrders();
};

/* ========================
 * 生命周期
 * ======================== */
onMounted(() => {
  loadOrders();

  const waitForAMap = () => {
    if (window.AMap && window.AMap.Map) {
      initMap();
    } else {
      setTimeout(waitForAMap, 100);
    }
  };

  waitForAMap();
});
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

.map {
  width: 100%;
  height: 360px;
  background: #f2f2f2;
  margin-bottom: 16px;
  position: relative;
}

.map-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
}

button {
  margin-right: 8px;
  margin-top: 6px;
  padding: 6px 12px;
}

li {
  border: 1px solid #ddd;
  padding: 12px;
  margin-bottom: 12px;
  list-style: none;
}
</style>
