export const SideBarModule = {
    namespaced: true,
    state: {
      sideBarDefaultActive: "1", // 当前激活菜单的第一项
      navName: "", // 面包屑导航名称
    },
    mutations: {
      // 处理侧边栏激活项
      SIDEBAE_DEFAULTACTIVE(state, data) {
        const { index, path } = data;
        state.sideBarDefaultActive = index;
        // 持久化处理
        localStorage.setItem("sideBarDefaultActive", index);
        localStorage.setItem("sideBarDefaultOpened", JSON.stringify([path[0]]));
      },
      // 处理面包屑导航
      NAV_NAME(state, name) {
        state.navName = name;
        localStorage.setItem("navName", name);
      },
    },
  };