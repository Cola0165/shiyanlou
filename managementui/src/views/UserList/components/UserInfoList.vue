<template>
  <div class="infolist">
    <!-- 客户列表信息 -->
    <el-row style="width:100%">
      <el-col style="width:100%">
        <el-card shadow="always">
          <!-- 表格按钮 -->
          <div class="judgebtn">
            <span class="newbtn">
              <!-- 新增用户信息 -->
              <UserNewInfo />
            </span>
          </div>
          <!-- 客户信息表格 -->
          <el-table
            ref="multipleTable"
            :data="tableData"
            border
            tooltip-effect="dark"
            style="width: 100%"
            @selection-change="handleSelectionChange"
          >
            <el-table-column label="序号" align="center" width="60">
              <template slot-scope="scope">{{ scope.row.date }}</template>
            </el-table-column>
            <el-table-column prop="name" label="姓名" align="center" />
            <el-table-column prop="carNum" label="车牌号码" align="center" />
            <el-table-column
              prop="allProtectMoney"
              label="总保费(元)"
              align="center"
            />
            <el-table-column prop="agent" label="坐席" align="center" />
            <el-table-column
              prop="Effectiveness"
              label="有效性"
              align="center"
            />
            <el-table-column
              prop="telnum"
              label="手机号码"
              width="300"
              align="center"
            >
              <!-- 电话号码选择框 -->
              <el-col :span="16">
                <el-select v-model="value" placeholder="请选择" size="mini">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-col>
              <!-- 电话，短信按钮 -->
              <el-col :span="8">
                <el-button type="warning" icon="el-icon-phone" circle />
                <el-button type="success" icon="el-icon-message" circle />
              </el-col>
            </el-table-column>
            <!-- 查看和编辑按钮 -->
            <el-table-column width="150" label="操作" align="center">
              <el-button
                type="primary"
                icon="el-icon-view"
                round
                size="mini"
                @click="btnRoute"
                >查看</el-button
              >
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import UserNewInfo from "./UserNewInfo.vue";
  export default {
    components: {
      UserNewInfo,
    },
    data() {
      return {
        tabpaneName: "first",
        dialogVisible: false,
        currentPage1: 5,
        dialogFormVisible: false,
        form: {
          name: "",
          userNum: "",
          carNum: "",
          allProtectList: "",
          allProtectMoney: "",
          protectNum: "",
          agent: "",
          customStatus: "",
          Effectiveness: "",
        },
        tableData: [
          {
            date: "1",
            name: "李光斌",
            userNum: "MCCM201951000160619539",
            carNum: "川A01202",
            allProtectList: "10",
            allProtectMoney: 855.0,
            protectNum: "PDZA201851010000501765",
            agent: "王莲",
            customStatus: "潜在客户",
            Effectiveness: "有效",
            telnum: 13886869890,
          },
        ],
        value: "13339876789",
        options: [
          {
            value: "电话1",
            label: "13978990987",
          },
          {
            value: "电话2",
            label: "15671879999",
          },
        ],
      };
    },
    methods: {
      btnRoute() {
        // 点击跳转路由的方法
        this.$router.push({
          path: "/userInfo",
        });
      },
      handleSelectionChange() {
        // todos
      },
    },
  };
</script>

<style scoped>
  .infolist {
    width: 100%;
    margin-top: 20px;
  }
  .judgebtn {
    height: 40px;
  }
  .newbtn {
    float: right;
    padding-right: 1%;
  }
</style>