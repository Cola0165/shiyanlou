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
      <el-table-column
        align="center"
        prop="numsTodayTotal"
        label="总待办数"
        width="150"
      >
        <template slot-scope="scope">
          <el-badge :value="scope.row.numsTodayTotal" type="primary">
            <el-button size="mini">总待办数</el-button>
          </el-badge>
        </template>
      </el-table-column>
      <el-table-column align="center" label="电销任务数" prop="telSales">
        <template slot-scope="scope">
          <el-row>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.telSales.totalTelSales"
                class="item"
                type="primary"
              >
                <el-button size="mini">总数</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.telSales.finishTelSales"
                class="item"
                type="success"
              >
                <el-button size="mini">已完成</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.telSales.unfinishTelSales"
                class="item"
              >
                <el-button size="mini">未完成</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.telSales.unfirstCallTelSales"
                class="item"
              >
                <el-button size="mini">未首呼</el-button>
              </el-badge>
            </el-col>
          </el-row>
        </template>
      </el-table-column>
      <el-table-column
        align="center"
        prop="marketing"
        label="营销任务数"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="scope">
          <el-row>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.marketing.totalMarketing"
                class="item"
                type="primary"
              >
                <el-button size="mini">总数</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.marketing.finishMarketing"
                class="item"
                type="success"
              >
                <el-button size="mini">已完成</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.marketing.unfinishMarketing"
                class="item"
              >
                <el-button size="mini">未完成</el-button>
              </el-badge>
            </el-col>
            <el-col :span="6" align="center" class="margin-bottom1">
              <el-badge
                :value="scope.row.marketing.unfirstCallMarketing"
                class="item"
              >
                <el-button size="mini">未首呼</el-button>
              </el-badge>
            </el-col>
          </el-row>
        </template>
      </el-table-column>
    </el-table>
    <el-divider />

    <el-form :inline="true" class="filter-box">
      <el-form-item label="时间段筛选">
        <el-date-picker
          v-model="value2"
          type="daterange"
          align="right"
          unlink-panels
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          size="mini"
          :picker-options="pickerOptions"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" size="mini" icon="el-icon-search"
          >查询</el-button
        >
      </el-form-item>
    </el-form>
    <!-- 默认列出一周内的待办任务 -->
    <div class>
      <el-table
        current-row-key
        :data="tableData"
        style="width: 100%"
        border
        fit
        highlight-current-row
      >
        <el-table-column label="任务来源" align="center" prop="origin">
          <template slot-scope="scope">
            <el-tag :type="scope.row.origin === '电销' ? 'primary' : 'success' "
              >{{ scope.row.origin }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column align="center" prop="nameCustomer" label="客户名称" />
        <el-table-column align="center" prop="numLicensePlate" label="车牌号" />
        <el-table-column align="center" prop="stateFirstCall" label="首呼状态">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.stateFirstCall === '未首呼' ? 'danger' : 'primary'"
              >{{ scope.row.stateFirstCall }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column
          align="center"
          prop="statusCustomer"
          label="客户状态"
        />
        <el-table-column align="center" label="起止时间">
          <template slot-scope="scope">
            <el-tag type="info" size="mini">{{ scope.row.startTime }}</el-tag>
            <el-tag type="info" size="mini">{{ scope.row.stopTime }}</el-tag>
          </template>
        </el-table-column>

        <el-table-column align="center" label="是否预约">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.isReservation === '预约' ? 'danger' : 'primary'"
              >{{ scope.row.isReservation }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column
          align="center"
          label="操作"
          class-name="small-padding fixed-width"
          width="300"
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
  </div>
</template>
<script>
  import Layout from "@/Layout";

  export default {
    data() {
      return {
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
        taskDealDetailShow: false,
        summary: [
          {
            numsTodayTotal: 104,
            telSales: {
              totalTelSales: 52,
              finishTelSales: 32,
              unfinishTelSales: 20,
              firstCallTelSales: 36,
              unfirstCallTelSales: 16,
            },
            marketing: {
              totalMarketing: 52,
              finishMarketing: 32,
              unfinishMarketing: 20,
              firstCallMarketing: 36,
              unfirstCallMarketing: 16,
            },
          },
        ],
        tableData: [
          {
            origin: "电销",
            nameCustomer: "李光斌",
            numLicensePlate: "川AY06M7",
            stateFirstCall: "未首呼",
            statusCustomer: "潜在客户",
            startTime: "2019-06-30",
            stopTime: "2020-06-30",
            isReservation: "预约",
          },
          {
            origin: "营销",
            nameCustomer: "王红霞",
            numLicensePlate: "川A1860V",
            stateFirstCall: "未首呼",
            statusCustomer: "潜在客户",
            startTime: "2019-06-30",
            stopTime: "2020-06-30",
            isReservation: "分配",
          },
        ],
      };
    },
    watch: {
      activeName(val) {
        this.$router.push(`${this.$route.path}?tab=${val}`); // 切换路由
      },
    },
    created() {
      const tab = this.$route.query.tab;
      if (tab) {
        this.activeName = tab;
      }
    },
    methods: {
      // 显示今日待办列表
      handleShowList() {
        this.listVisible = true;
      },
      // 查看客户信息
      showDetail() {
        const id = parseInt(Math.random() * 100000);
        const route = {
          path: `/userInfo?id=${id}`,
          component: Layout,
          hidden: true,
        };
        this.$router.push(route);
      },
      // 弹出弹框
      showTaskDealDetail() {
        this.$refs.childHandle.showDialog();
      },
    },
  };
</script>
<style>
  .el-badge__content.is-fixed {
    top: 8px !important;
  }
</style>

<style scoped>
  .margin-bottom1 {
    margin-bottom: 3px;
  }
  .filter-box {
    margin-top: 15px;
  }
</style>