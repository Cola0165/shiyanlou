<template>
  <div class="ui-task-today">
    <el-table
      current-row-key
      :data="summary"
      style="width: 100%"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" prop="finishTask" label="已完成任务">
        <template slot-scope="scope">
          <el-badge :value="scope.row.finishTask" class type="primary">
            <el-button size="mini">已完成</el-button>
          </el-badge>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="totalTask" label="总的完成数">
        <template slot-scope="scope">
          <el-badge :value="scope.row.totalTask" class type="primary">
            <el-button size="mini">总完成</el-button>
          </el-badge>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="monthTask" label="本月完成数">
        <template slot-scope="scope">
          <el-badge :value="scope.row.monthTask" class type="success">
            <el-button size="mini">本月完成</el-button>
          </el-badge>
        </template>
      </el-table-column>
    </el-table>
    <el-divider />

    <el-form :inline="true" class="margin-top15">
      <el-form-item label="时间段筛选">
        <el-date-picker
          type="daterange"
          align="right"
          unlink-panels
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          size="mini"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" size="mini" icon="el-icon-search"
          >查询</el-button
        >
      </el-form-item>
    </el-form>
    <!-- 默认列出一周内的已完成任务 -->
    <el-table
      current-row-key
      :data="tableData"
      style="width: 100%"
      border
      fit
      highlight-current-row
      class="margin-top15"
    >
      <el-table-column align="center" prop="nameTask" label="任务名称" />
      <el-table-column align="center" prop="nameNode" label="节点名称" />
      <el-table-column align="center" prop="nameCustomer" label="客户名称" />
      <el-table-column align="center" prop="numLicensePlate" label="车牌号" />
      <el-table-column align="center" prop="finishtime" label="完成时间" />
      <el-table-column align="center" label="起止时间">
        <template slot-scope="scope">
          <el-tag type="info" size="mini">{{ scope.row.startTime }}</el-tag>
          <el-tag type="info" size="mini">{{ scope.row.stopTime }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column
        align="center"
        label="操作"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="{row}">
          <el-button
            type="success"
            size="small"
            icon="el-icon-service"
            @click="handleUpdate(row)"
            >回访</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        summary: [
          {
            finishTask: 269,
            totalTask: 300,
            monthTask: 66,
          },
        ],
        tableData: [
          {
            nameTask: "续保服务中心2019051701",
            nameNode: "续保团队单节点",
            nameCustomer: "李光斌",
            numLicensePlate: "川AY04M7",
            startTime: "2019-06-30",
            stopTime: "2020-06-29",
            finishtime: "2018-06-30 12:34:88",
          },
          {
            nameTask: "续保服务中心2019051701",
            nameNode: "续保团队单节点",
            nameCustomer: "肖兵",
            numLicensePlate: "川AS94B0",
            startTime: "2019-06-30",
            stopTime: "2020-06-29",
            finishtime: "2018-06-30 12:34:88",
          },
          {
            nameTask: "续保服务中心2019051701",
            nameNode: "续保团队单节点",
            nameCustomer: "李翼",
            numLicensePlate: "川A94U8Q",
            startTime: "2019-06-30",
            stopTime: "2020-06-29",
            finishtime: "2018-06-30 12:34:88",
          },
        ],
      };
    },
  };
</script>
<style scoped>
  .margin-top15 {
    margin-top: 15px;
  }
</style>