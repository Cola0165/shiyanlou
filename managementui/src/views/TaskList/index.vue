<template>
  <div class="app-container">
    <el-card>
      <el-tabs v-model="activeName" type="border-card">
        <el-tab-pane
          :key="tabMapOptions[0].key"
          :label="tabMapOptions[0].label"
          :name="tabMapOptions[0].key"
        >
          <keep-alive>
            <task-todo
              v-if="activeName==tabMapOptions[0].key"
              :type="tabMapOptions[0].key"
            />
          </keep-alive>
        </el-tab-pane>

        <el-tab-pane
          :key="tabMapOptions[1].key"
          :label="tabMapOptions[1].label"
          :name="tabMapOptions[1].key"
        >
          <keep-alive>
            <task-reservation
              v-if="activeName==tabMapOptions[1].key"
              :type="tabMapOptions[1].key"
            />
          </keep-alive>
        </el-tab-pane>

        <el-tab-pane
          :key="tabMapOptions[2].key"
          :label="tabMapOptions[2].label"
          :name="tabMapOptions[2].key"
        >
          <keep-alive>
            <task-finish
              v-if="activeName==tabMapOptions[2].key"
              :type="tabMapOptions[2].key"
            />
          </keep-alive>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>
<script>
  import taskTodo from "./components/TaskTodo";
  import taskFinish from "./components/TaskFinish";
  import taskReservation from "./components/TaskReservation";

  export default {
    name: "TaskList",
    components: {
      "task-todo": taskTodo,
      "task-finish": taskFinish,
      "task-reservation": taskReservation,
    },
    data() {
      return {
        tabMapOptions: [
          { label: "待办任务", key: "taskTodo" },
          { label: "预约任务", key: "taskReservation" },
          { label: "已完成任务", key: "taskFinish" },
        ],
        activeName: "taskTodo",
      };
    },
  };
</script>
<style scoped>
  .app-container {
    position: relative;
    padding: 10px;
  }
</style>