<template>
  <div class="header-container">
    <el-breadcrumb separator="/" class="breadcrumb">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="drop-down">
      <el-dropdown>
        <span class="el-dropdown-link">
          用户A
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>
<script>
  import { mapState } from "vuex";
  export default {
    data() {
      return {
        name: this.navName || "",
      };
    },
    computed: {
      ...mapState({
        navName: (state) => state.SIDEBAR.navName, // 从 state 中获取 navName 的值
      }),
    },
    mounted() {
      this.name = localStorage.getItem("navName") || "";
    },
    watch: {
      navName(newVal) {
        console.info(newVal);
        this.name = newVal;
      },
    },
  };
</script>
<style scoped>
  .header-container {
    position: relative;
    width: 100%;
    height: 40px;
    background: #fff;
  }
  .breadcrumb {
    position: absolute;
    top: 15px;
    left: 15px;
  }
  .drop-down {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
  }
</style>