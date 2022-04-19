<template slot-scope="scope">
  <div id="basis" class="app-container">
    <el-tabs type="border-card">
      <el-tab-pane label="客户信息">
        <div>
          <Basis />
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  import Basis from "./components/Basis";

  export default {
    components: {
      Basis,
    },
  };
</script>

<style scoped>
  .app-container {
    padding: 10px;
  }
</style>