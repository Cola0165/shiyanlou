<template>
  <div class="app-container">
    <el-card>
      <UserSearch />
      <UserSearchList />
    </el-card>
  </div>
</template>

<script>
  import UserSearchList from "./components/UserInfoList.vue";
  import UserSearch from "./components/UserSearch.vue";

  export default {
    components: {
      UserSearchList,
      UserSearch,
    },
  };
</script>

<style scoped>
  .app-container {
    padding: 10px;
  }
</style>