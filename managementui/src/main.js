import Vue from "vue";
import ElementUI from "element-ui"; // 引入 ElementUI 组件库
import "element-ui/lib/theme-chalk/index.css"; // ElementUI 的样式文件需要单独引入
import App from "./App.vue";
// 引入路由和路由配置
import VueRouter from "vue-router";
import routerConfig from "@/router";
import store from "@/store"; // 引入 store

Vue.config.productionTip = false;
Vue.use(ElementUI);
// 使用路由
Vue.use(VueRouter);
// 生成路由实例
const router = new VueRouter(routerConfig);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");