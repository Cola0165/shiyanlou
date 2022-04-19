export default {
    data() {
      return {
        $_sidebarElm: null,
      };
    },
    mounted() {
      this.$_initResizeEvent();
      this.$_initSidebarResizeEvent();
    },
    beforeDestroy() {
      this.$_destroyResizeEvent();
      this.$_destroySidebarResizeEvent();
    },
    // 当被 keep-live 缓存时修复存在的问题
    activated() {
      this.$_initResizeEvent();
      this.$_initSidebarResizeEvent();
    },
    deactivated() {
      this.$_destroyResizeEvent();
      this.$_destroySidebarResizeEvent();
    },
    methods: {
      // 使用 $_ 用于混合属性，一下属性
      $_resizeHandler() {
        return function () {
          if (this.chart) {
            this.chart.resize();
          }
        };
      },
      $_initResizeEvent() {
        // 监听 resize 事件
        window.addEventListener("resize", this.$_resizeHandler);
      },
      $_destroyResizeEvent() {
        window.removeEventListener("resize", this.$_resizeHandler);
      },
      $_sidebarResizeHandler(e) {
        if (e.propertyName === "width") {
          this.$_resizeHandler();
        }
      },
      $_initSidebarResizeEvent() {
        this.$_sidebarElm =
          document.getElementsByClassName("sidebar-container")[0];
        this.$_sidebarElm &&
          this.$_sidebarElm.addEventListener(
            "transitionend",
            this.$_sidebarResizeHandler
          );
      },
      $_destroySidebarResizeEvent() {
        this.$_sidebarElm &&
          this.$_sidebarElm.removeEventListener(
            "transitionend",
            this.$_sidebarResizeHandler
          );
      },
    },
  };