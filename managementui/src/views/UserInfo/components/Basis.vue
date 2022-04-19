<template>
  <div>
    <!-- 基本信息 -->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span style="text-align: left; font-size: 15px"
          ><i class="el-icon-document" />&nbsp;基本信息</span
        >
        <el-button
          type="primary"
          icon="el-icon-upload"
          style="float: right; padding: 5px"
          >保存</el-button
        >
        <el-button
          type="warning"
          style="float: right; padding: 5px;margin-right:10px"
          icon="el-icon-time"
          @click="dialogVisible = true"
          >预约/跟进状态</el-button
        >
        <!-- 预约信息对话框 -->
        <el-dialog :visible.sync="dialogVisible" width="60%" title="预约">
          <div slot="header" class="clearfix">
            <span>姓名:王小小</span>
            <span style="display:inline-block;margin-left:20px"
              >电话:1808009999</span
            >
          </div>
          <!-- 中间部分 -->
          <el-form
            ref="form"
            v-model="labelPosition"
            :inline="true"
            :model="form"
            label-width="100px"
          >
            <el-form-item label="预约时间">
              <el-date-picker
                v-model="value1"
                type="datetime"
                placeholder="选择日期时间"
                style="width:200px;"
              />
            </el-form-item>
            <el-form-item label="任务状态">
              <el-select
                v-model="value"
                placeholder="状态1"
                style="width:200px;"
              >
                <el-option
                  v-for="item in options2"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="跟进状态">
              <el-select
                v-model="value"
                placeholder="状态1"
                style="width:200px;"
              >
                <el-option
                  v-for="item in options2"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="备注">
              <el-input
                v-model="form.name"
                type="textarea"
                :autosize="{ minRows: 2, maxRows: 20}"
                placeholder="请输入内容"
                style="width:300px;"
              />
            </el-form-item>
            <el-button
              size="mini"
              style="float:right;margin-top:10px"
              icon="el-icon-close"
              @click="dialogVisible = false"
              >取 消</el-button
            >
            <el-button
              type="primary"
              size="mini"
              style="float:right;margin-top:10px;margin-right:10px"
              icon="el-icon-check"
              @click="dialogVisible = false"
              >保存</el-button
            >
          </el-form>
        </el-dialog>
      </div>

      <!-- 基本信息 -->
      <el-form
        ref="form"
        v-model="labelPosition"
        :inline="true"
        :model="form"
        label-width="80px"
      >
        <el-form-item label="客户姓名">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>
        <el-form-item label="性别" :inline="false">
          <el-select
            v-model="form.region"
            placeholder="请选择性别"
            class="width220"
          >
            <el-option label="男" value="shanghai" />
            <el-option label="女" value="beijing" />
          </el-select>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>
        <el-form-item label="证件类型">
          <el-select
            v-model="form.region"
            placeholder="证件类型"
            class="width220"
          >
            <el-option label="身份证" value="shanghai" />
            <el-option label="军官证" value="beijing" />
          </el-select>
        </el-form-item>
        <el-form-item label="证件号码">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>

        <el-form-item label="省市区">
          <el-cascader
            v-model="selectedOptions2"
            expand-trigger="hover"
            :options="options"
            class="width220"
            @change="handleChange"
          />
        </el-form-item>
        <el-form-item label="地址">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>
        <el-form-item label="邮政编码">
          <el-input v-model="form.name" class="width220" />
        </el-form-item>

        <!--  更多信息 -->
        <el-collapse v-model="activeNames" @change="handleChange">
          <el-collapse-item title="更多信息" name="1">
            <el-form-item label="客户ID" style="width:300px;">
              <el-input v-model="form.carNum" />
            </el-form-item>
            <el-form-item label="手机号码" :label-width="width90">
              <el-select
                v-model="form.region"
                placeholder="手机号码"
                class="width210"
              >
                <el-option label="13332334321" value="shanghai" />
                <el-option label="16771212121" value="beijing" />
              </el-select>
            </el-form-item>
            <el-form-item label="客户类型" :label-width="width90">
              <el-input v-model="form.name" class="width210" />
            </el-form-item>
            <el-form-item label="推荐送修码" :label-width="width90">
              <el-input v-model="form.name" class="width210" />
            </el-form-item>
            <el-form-item label="出生日期" :label-width="width90">
              <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期"
                class="width210"
              />
            </el-form-item>
            <el-form-item label="户口所在地" :label-width="width90">
              <el-cascader
                v-model="selectedOptions2"
                expand-trigger="hover"
                :options="options"
                class="width210"
                @change="handleChange"
              />
            </el-form-item>
          </el-collapse-item>
          <!-- 2 联系方式 -->
          <el-collapse-item title="联系方式" name="3">
            <!-- 联系方式 -->
            <el-button
              style="float: right; padding: 5px;margin-bottom:10px;"
              type="success"
              icon="el-icon-circle-plus-outline"
              @click="appendContact"
              >追加</el-button
            >
            <el-table
              :data="contactData"
              border
              style="width: 100%;margin-bottom:10px;"
            >
              <el-table-column align="center" prop="type" label="电话类型">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.type"
                    placeholder="电话类型"
                    clearable
                    size="mini"
                  />
                </template>
              </el-table-column>
              <el-table-column align="center" prop="nums" label="号码">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.nums"
                    placeholder="号码"
                    maxlength="11"
                    clearable
                    size="mini"
                  />
                </template>
              </el-table-column>
              <el-table-column align="center" prop="name" label="联系人姓名">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.name"
                    placeholder="联系人姓名"
                    clearable
                    size="mini"
                  />
                </template>
              </el-table-column>

              <el-table-column
                align="center"
                prop="isForbident"
                label="禁拨名单"
              >
                <template slot-scope="scope">
                  <el-select
                    v-model="scope.row.isForbident"
                    placeholder="否"
                    size="mini"
                  >
                    <el-option label="是" value="shanghai" />
                    <el-option label="否" value="beijing" />
                  </el-select>
                </template>
              </el-table-column>
              <el-table-column align="center" prop="isUseful" label="有效性">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.isUseful"
                    size="mini"
                    placeholder="有效性"
                    clearable
                  />
                </template>
              </el-table-column>
              <el-table-column
                align="center"
                prop="isDefaultPhone"
                label="是否默认"
              >
                <template slot-scope="scope">
                  <el-select
                    v-model="scope.row.isDefaultPhone"
                    placeholder="是否默认"
                    size="mini"
                  >
                    <el-option label="是" value="是" />
                    <el-option label="否" value="否" />
                  </el-select>
                </template>
              </el-table-column>
              <el-table-column label="操作" align="center">
                <el-col :span="24">
                  <el-button type="success" icon="el-icon-phone" circle />
                  <el-button type="warning" icon="el-icon-message" circle />
                </el-col>
              </el-table-column>
            </el-table>
          </el-collapse-item>
        </el-collapse>
      </el-form>
    </el-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        width90: "90px",
        value: "",
        value1: "",
        dialogVisible: false,
        labelPosition: "right",
        activeNames: ["3"],
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
        options2: [
          {
            value: "选项1",
            label: "状态1",
          },
          {
            value: "选项2",
            label: "状态2",
          },
        ],
        options: [
          {
            value: "zhinan",
            label: "四川省",
            children: [
              {
                value: "shejiyuanze",
                label: "成都市",
                children: [
                  {
                    value: "yizhi",
                    label: "武侯区",
                  },
                  {
                    value: "fankui",
                    label: "双流区",
                  },
                  {
                    value: "xiaolv",
                    label: "金牛区",
                  },
                  {
                    value: "kekong",
                    label: "青羊区",
                  },
                ],
              },
              {
                value: "daohang",
                label: "眉山市",
                children: [
                  {
                    value: "cexiangdaohang",
                    label: "眉山1区",
                  },
                  {
                    value: "dingbudaohang",
                    label: "眉山2区",
                  },
                ],
              },
            ],
          },
          {
            value: "zhinan",
            label: "湖北省",
            children: [
              {
                value: "shejiyuanze",
                label: "武汉市",
                children: [
                  {
                    value: "yizhi",
                    label: "武侯区",
                  },
                  {
                    value: "fankui",
                    label: "双流区",
                  },
                  {
                    value: "xiaolv",
                    label: "金牛区",
                  },
                  {
                    value: "kekong",
                    label: "青羊区",
                  },
                ],
              },
              {
                value: "daohang",
                label: "恩施市",
                children: [
                  {
                    value: "cexiangdaohang",
                    label: "眉山1区",
                  },
                  {
                    value: "dingbudaohang",
                    label: "眉山2区",
                  },
                ],
              },
            ],
          },
        ],
        selectedOptions: [],
        selectedOptions2: [],
        contactData: [
          {
            type: "手机",
            nums: "1398079410",
            name: "王萱荣",
            isImportant: "否",
            isForbident: "否",
            isUseful: "有效",
            isDefaultPhone: "是",
          },
        ],
      };
    },
    methods: {
      handleChange(val) {
        console.log(val);
      },
      appendContact() {
        const newData = {
          type: "电话",
          nums: "021-88729823",
          name: "王萱荣",
          isImportant: "否",
          isForbident: "否",
          isUseful: "有效",
          isDefaultPhone: "是",
        };
        this.contactData.splice(0, 0, newData);
      },
    },
  };
</script>

<style scoped>
  .mt-20 {
    margin-top: 20px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .width220 {
    width: 220px;
  }
  .width210 {
    width: 210px;
  }
</style>