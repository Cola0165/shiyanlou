<template>
  <el-menu
    :default-openeds="defaultOpened"
    :default-active="defaultActive"
    @select="handleSelect"
  >
    <router-link to="/">
      <el-menu-item index="1">
        <i class="el-icon-s-home"></i>首页
      </el-menu-item>
    </router-link>
    <router-link to="/tasklist">
      <el-menu-item index="2">
        <i class="el-icon-s-order"></i>任务列表
      </el-menu-item>
    </router-link>
    <el-submenu index="3">
      <template slot="title">
        <i class="el-icon-user-solid"></i>客户管理
      </template>
      <router-link to="/userList">
        <el-menu-item index="3-1">客户列表</el-menu-item>
      </router-link>
      <router-link to="/userInfo">
        <el-menu-item index="3-2">客户信息</el-menu-item>
      </router-link>
    </el-submenu>
  </el-menu>
</template>
<script>
  import { mapMutations } from "vuex";
  export default {
    data() {
      return {
        defaultActive: "1",
        defaultOpened: [],
        navMenuNames: [
          { index: "2", name: "任务列表" },
          { index: "3-1", name: "客户列表" },
          { index: "3-2", name: "客户信息" },
        ],
      };
    },
    mounted() {
      // 从 localStorage 中获取名称为 sideBarDefaultActive 与 sideBarDefaultOpened 的值
      const sideBarDefaultActive =
        localStorage.getItem("sideBarDefaultActive") || "1";
      const sideBarDefaultOpened =
        localStorage.getItem("sideBarDefaultOpened") || [];
      this.defaultActive = sideBarDefaultActive;
      this.defaultOpened = JSON.parse(sideBarDefaultOpened);
    },
    methods: {
      ...mapMutations("SIDEBAR", ["SIDEBAE_DEFAULTACTIVE", "NAV_NAME"]),
      handleSelect(index, path) {
        const data = {
          index,
          path,
        };
        // 调用 SIDEBAE_DEFAULTACTIVE 这个 mutation
        this.SIDEBAE_DEFAULTACTIVE(data);
        const navName = this.navMenuNames.filter(
          (item) => item.index === index
        );
        if (navName.length > 0) {
          this.NAV_NAME(navName[0].name); // 调用 NAV_NAME 这个 mutation
        } else {
          this.NAV_NAME("");
        }
      },
    },
  };
</script>
<style>
  a {
    text-decoration: none;
    color: inherit;
  }
  .el-menu {
    border: none;
  }
  .el-menu-item:hover,
  .el-submenu__title:hover {
    background-color: #233142;
  }
  .el-menu-item,
  .el-submenu__title {
    height: 56px;
    line-height: 56px;
    font-size: 14px;
    color: rgb(191, 203, 217);
    padding: 0 20px;
    list-style: none;
    cursor: pointer;
    position: relative;
    text-align: left;
    -webkit-transition: border-color 0.3s, background-color 0.3s, color 0.3s;
    transition: border-color 0.3s, background-color 0.3s, color 0.3s;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    white-space: nowrap;
    background-color: rgb(48, 65, 86);
  }

  .el-menu-item.is-active {
    color: #1890ff;
    background-color: #233142;
  }
</style>