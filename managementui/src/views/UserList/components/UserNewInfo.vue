<template>
  <div>
    <el-button
      type="primary"
      icon="el-icon-edit-outline"
      size="mini"
      @click="dialogVisible = true"
      >新增</el-button
    >

    <el-dialog
      title
      :visible.sync="dialogVisible"
      width="55%"
      :before-close="handleClose"
    >
      <h2 style="text-align: left; font-size: 20px;margin-top:-30px">
        <i
          class="el-icon-circle-plus

"
        ></i
        >客户新增
      </h2>
      <el-card class="box-card">
        <el-form
          ref="form"
          v-model="labelPosition"
          :inline="true"
          :model="form"
          label-width="120px"
          size="mini"
        >
          <el-form-item label="客户姓名">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="证件类型">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="证件号码">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="联系类型">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="联系号码">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="联系方式验证">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="车牌号">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="车驾号">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="推荐送修码">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="承保公司">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
          <el-form-item label="终保日期">
            <el-input v-model="form.name" style="width: 200px;" />
          </el-form-item>
        </el-form>
        <el-button
          @click="dialogVisible = false"
          icon="el-icon-close"
          size="mini"
          style="float:right;margin-top:10px;margin-bottom:10px"
          >取 消</el-button
        >
        <el-button
          type="primary"
          @click="dialogVisible = false"
          icon="el-icon-check"
          size="mini"
          style="float:right;margin-top:10px;margin-bottom:10px;margin-right:10px"
          >确 定</el-button
        >
      </el-card>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeNames: ["1"],
        labelPosition: "left",
        dialogVisible: false,
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
      };
    },
    methods: {
      handleClose() {
        // todos
      },
    },
  };
</script>