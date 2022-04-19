import Vue from "vue";
import Vuex from "vuex";
import { SideBarModule } from "./modules/sideBar";
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    SIDEBAR: SideBarModule,
  },
});