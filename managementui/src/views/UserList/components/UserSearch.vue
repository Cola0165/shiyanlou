<template>
  <div class="search">
    <!-- 折叠表头 -->
    <el-card>
      <el-collapse>
        <el-collapse-item name="1">
          <template slot="title">
            <i class="el-icon-search" />&nbsp;客户信息查询
          </template>
          <!-- 客户信息查询 -->
          <el-form
            ref="form"
            v-model="labelPosition"
            :inline="true"
            :model="form"
            label-width="100px"
            class="padding-bottom15"
          >
            <el-row>
              <el-col :span="8">
                <el-form-item label="客户姓名">
                  <el-input v-model="form.name" />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="车牌号码">
                  <el-input v-model="form.carNum" />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="保单号" :inline="false">
                  <el-input v-model="form.name" />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="手机号码">
                  <el-input v-model="form.name" />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="证件类型">
                  <el-select
                    v-model="form.region"
                    placeholder="请选择证件类型"
                    class="width185"
                  >
                    <el-option label="学生证" value="shanghai" />
                    <el-option label="军官证" value="beijing" />
                  </el-select>
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="证件号码">
                  <el-input v-model="form.name" />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="初保日期">
                  <el-date-picker
                    v-model="form.date1"
                    type="datetime"
                    class="width185"
                    placeholder="2019/08/02 14:00:00"
                  />
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="终保日期">
                  <el-date-picker
                    v-model="form.date1"
                    type="datetime"
                    class="width185"
                    placeholder="2022/08/02 14:00:00"
                  />
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="信息源" style="margin-bottom:-10px">
                  <el-checkbox
                    v-model="checkAll"
                    :indeterminate="isIndeterminate"
                    @change="handleCheckAllChange"
                    >全选</el-checkbox
                  >
                  <div style="margin: 15px 0;" />
                  <el-checkbox-group
                    v-model="checkedCities"
                    @change="handleCheckedCitiesChange"
                  >
                    <el-checkbox
                      v-for="city in cities"
                      :key="city"
                      :label="city"
                      >{{ city }}</el-checkbox
                    >
                  </el-checkbox-group>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-button
                  type="primary"
                  icon="el-icon-search"
                  style="position:relative;top:45px;"
                  @click="onSubmit"
                  >查询</el-button
                >
              </el-col>
            </el-row>
          </el-form>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </div>
</template>

<script>
  const cityOptions = ["营销", "电销", "微信公众号", "微博"]; // 复选框的值
  export default {
    data() {
      return {
        // 复选框数据信息
        checkAll: false,
        checkedCities: ["营销系统"],
        cities: cityOptions,
        isIndeterminate: true,
        activeNames: ["1"],
        labelPosition: "left",
        form: {
          region: "身份证",
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
      };
    },
    methods: {
      handleCheckAllChange(val) {
        this.checkedCities = val ? cityOptions : [];
        this.isIndeterminate = false;
      },
      handleCheckedCitiesChange(value) {
        const checkedCount = value.length;
        this.checkAll = checkedCount === this.cities.length;
        this.isIndeterminate =
          checkedCount > 0 && checkedCount < this.cities.length;
      },
      onSubmit() {
        console.log("submit!");
      },
    },
  };
</script>

<style scoped>
  .search {
    width: 100%;
  }
  .el-collapse .el-collapse-item {
    margin-bottom: 0;
  }
  .padding-bottom15 {
    padding-bottom: 15px;
  }
  .width185 {
    width: 185px;
  }
</style>