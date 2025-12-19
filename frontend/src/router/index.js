import { createRouter, createWebHistory } from "vue-router";
import CreateOrder from "../views/CreateOrder.vue";
import NearbyOrders from "../views/NearbyOrders.vue";

const routes = [
  {
    path: "/",
    redirect: "/nearby",
  },
  {
    path: "/create",
    component: CreateOrder,
  },
  {
    path: "/nearby",
    component: NearbyOrders,
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
