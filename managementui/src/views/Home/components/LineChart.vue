<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
  import * as echarts from "echarts"; // 引入 echarts
  require("echarts/theme/macarons"); // 使用 echarts 的 macarons 主题
  import resize from "./mixins/resize";

  export default {
    mixins: [resize],
    props: {
      className: {
        type: String,
        default: "chart",
      },
      width: {
        type: String,
        default: "100%",
      },
      height: {
        type: String,
        default: "350px",
      },
      autoResize: {
        type: Boolean,
        default: true,
      },
      chartData: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        chart: null,
      };
    },
    watch: {
      chartData: {
        deep: true,
        handler(val) {
          this.setOptions(val);
        },
      },
    },
    mounted() {
      this.$nextTick(() => {
        this.initChart();
      });
    },
    beforeDestroy() {
      if (!this.chart) {
        return;
      }
      this.chart.dispose();
      this.chart = null;
    },
    methods: {
      initChart() {
        this.chart = echarts.init(this.$el, "macarons"); // 初始化 echarts 实例对象
        this.setOptions(this.chartData);
      },
      //  echarts 的配置信息
      setOptions({ expectedData, actualData } = {}) {
        // 设置 echart 的 option 字段值
        this.chart.setOption({
          xAxis: {
            data: ["一月", "二月", "三月", "四月", "五月", "六月", "七月"],
            boundaryGap: false,
            axisTick: {
              show: false,
            },
          },
          grid: {
            left: 10,
            right: 10,
            bottom: 20,
            top: 30,
            containLabel: true,
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross",
            },
            padding: [5, 10],
          },
          yAxis: {
            axisTick: {
              show: false,
            },
          },
          legend: {
            data: ["期望", "实际"],
          },
          series: [
            {
              name: "期望",
              itemStyle: {
                normal: {
                  color: "#FF005A",
                  lineStyle: {
                    color: "#FF005A",
                    width: 2,
                  },
                },
              },
              smooth: true,
              type: "line",
              data: expectedData,
              animationDuration: 2800,
              animationEasing: "cubicInOut",
            },
            {
              name: "实际",
              smooth: true,
              type: "line",
              itemStyle: {
                normal: {
                  color: "#3888fa",
                  lineStyle: {
                    color: "#3888fa",
                    width: 2,
                  },
                  areaStyle: {
                    color: "#f3f8ff",
                  },
                },
              },
              data: actualData,
              animationDuration: 2800,
              animationEasing: "quadraticOut",
            },
          ],
        });
      },
    },
  };
</script>
<style scoped>
  .chart {
    background: #fff;
  }
</style>