<template>
  <div class="container">
    <h2>发布订单</h2>

    <div class="form-item">
      <label>订单描述</label>
      <input v-model="form.desc" placeholder="如：帮我取一个快递" />
    </div>

    <div class="form-item">
      <label>地址</label>
      <input v-model="form.address" placeholder="如：教学楼 A 座" />
    </div>

    <div class="form-item">
      <label>纬度 (lat)</label>
      <input type="number" v-model.number="form.lat" />
    </div>

    <div class="form-item">
      <label>经度 (lng)</label>
      <input type="number" v-model.number="form.lng" />
    </div>

    <button @click="submitOrder">提交订单</button>

    <p v-if="result">{{ result }}</p>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import request from "../api/request";

const result = ref("");

const form = reactive({
  userId: 1, // 演示用固定用户
  desc: "",
  address: "",
  lat: 39.9155,
  lng: 116.4345,
});

const submitOrder = async () => {
  try {
    const res = await request.post("/order/create", form);
    result.value = `订单创建成功，ID = ${res.data.orderId}`;
  } catch (e) {
    result.value = "创建失败，请确认后端是否启动";
  }
};
</script>

<style scoped>
.container {
  max-width: 420px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}

.form-item {
  margin-bottom: 12px;
}

label {
  display: block;
  font-size: 14px;
  margin-bottom: 4px;
}

input {
  width: 100%;
  padding: 6px;
}

button {
  margin-top: 10px;
  padding: 8px 12px;
  cursor: pointer;
}
</style>
