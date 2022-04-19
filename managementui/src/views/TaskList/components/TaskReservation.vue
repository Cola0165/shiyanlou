<template>
  <div class="ui-task-reservation">
    <el-collapse accordion>
      <el-collapse-item :class="['collapse-item_header']">
        <template slot="title" style="color:red">
          <i class="el-icon-search" />&nbsp;查询客户
        </template>
        <el-form
          :label-position="labelPosition"
          :inline="true"
          :model="formInline"
          label-width="100px"
          size="mini"
        >
          <el-form-item label="客户姓名">
            <el-input
              v-model="formInline.nameCustomer"
              placeholder="客户姓名"
            />
          </el-form-item>
          <el-form-item label="车牌号">
            <el-input
              v-model="formInline.numLicensePlate"
              placeholder="车牌号"
            />
          </el-form-item>
          <el-form-item label="预约优先级">
            <el-select v-model="formInline.level" placeholder="优先级">
              <el-option label="全部" value="0" />
              <el-option label="高" value="1" />
              <el-option label="中" value="2" />
              <el-option label="低" value="3" />
            </el-select>
          </el-form-item>
          <el-form-item label="跟进状态">
            <el-select
              v-model="formInline.stateTouch"
              placeholder="跟进状态"
              class="limitWidth"
            >
              <el-option label="继续跟踪" value="0" />
              <el-option label="成功" value="1" />
              <el-option label="失败" value="2" />
              <el-option label="未跟进" value="3" />
            </el-select>
          </el-form-item>
          <el-form-item label="预约时间">
            <el-date-picker
              v-model="value2"
              type="daterange"
              align="right"
              unlink-panels
              range-separator="~"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :picker-options="pickerOptions"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" icon="el-icon-search">查询</el-button>
          </el-form-item>
        </el-form>
      </el-collapse-item>
    </el-collapse>
    <!-- 默认列出3天内的预约任务 -->
    <el-table
      current-row-key
      :data="tableData"
      style="width: 100%"
      border
      fit
      highlight-current-row
    >
      <el-table-column
        align="center"
        prop="nameCustomer"
        label="客户姓名"
        width="80px"
      />
      <el-table-column align="center" prop="numLicensePlate" label="车牌号" />
      <el-table-column align="center" prop="level" label="优先级" width="80px">
        <template slot-scope="scope">
          <el-tag :type="scope.row.level === '高' ? 'danger' : 'primary'"
            >{{ scope.row.level }}</el-tag
          >
        </template>
      </el-table-column>
      <el-table-column align="center" prop="stateTouch" label="跟进状态">
        <template slot-scope="scope">
          <el-tag
            :type="scope.row.stateTouch === '继续跟踪' ? 'primary' : 'danger'"
            >{{ scope.row.stateTouch }}</el-tag
          >
        </template>
      </el-table-column>
      <el-table-column align="center" prop="timeReservation" label="预约时间">
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
          <el-button type="primary" size="small" icon="el-icon-phone"
            >联系客户</el-button
          >
          <el-button
            type="primary"
            size="small"
            icon="el-icon-view"
            @click="showDetail(row)"
            >查看客户信息</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
  import Layout from "@/Layout";
  export default {
    created() {
      const tab = this.$route.query.tab; // 获取路由中的 tab 字段值
      if (tab) {
        this.activeName = tab;
      }
    },
    methods: {
      showDetail() {
        const id = parseInt(Math.random() * 100000); // 随机生成一个 100000 以内的数值作为 id
        const route = {
          path: `/userInfo?id=${id}`,
          component: Layout,
          hidden: true,
        };
        this.$router.push(route);
      },
    },
    data() {
      return {
        labelPosition: "right",
        formInline: {
          nameCustomer: "",
          numLicensePlate: "",
          level: "高",
          stateTouch: "继续跟踪",
        },
        pickerOptions: {
          shortcuts: [
            {
              text: "最近一周",
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                picker.$emit("pick", [start, end]);
              },
            },
            {
              text: "最近一个月",
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                picker.$emit("pick", [start, end]);
              },
            },
            {
              text: "最近三个月",
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                picker.$emit("pick", [start, end]);
              },
            },
          ],
        },
        value2: "",
        tableData: [
          {
            nameCustomer: "李光斌",
            numLicensePlate: "川AY04M7",
            level: "高",
            stateTouch: "继续跟踪",
            startTime: "2019-06-30 12:00:00",
            stopTime: "2019-07-30 10:00:00",
          },
          {
            nameCustomer: "肖兵",
            numLicensePlate: "川AS94B0",
            level: "低",
            stateTouch: "继续跟踪",
            startTime: "2019-06-30 12:00:00",
            stopTime: "2019-07-30 10:00:00",
          },
          {
            nameCustomer: "李翼",
            numLicensePlate: "川A94U8Q",
            level: "中",
            stateTouch: "继续跟踪",
            startTime: "2019-06-30 12:00:00",
            stopTime: "2019-07-30 10:00:00",
          },
        ],
      };
    },
    watch: {
      // 监听 activeName 的变化
      activeName(val) {
        this.$router.push(`${this.$route.path}?tab=${val}`);
      },
    },
  };
</script>
<style scoped>
  .limitWidth {
    width: 185px;
  }
</style>

<style lang="scss">
  .el-collapse {
    .el-collapse-item {
      border-left: 1px solid #e6ebf5;
      border-right: 1px solid #e6ebf5;
      margin-bottom: 10px;
    }
    .el-collapse-item__header {
      padding-left: 10px;
      border-bottom: 1px solid #e6ebf5;
    }
    .el-collapse-item__content {
      padding: 0 10px;
      margin-top: 10px;
    }
  }
</style>