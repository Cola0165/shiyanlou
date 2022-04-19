// vue.config.js
const path = require("path");

function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  publicPath: "", // 公共路径
  productionSourceMap: false, // 生产环境不使用 sourceMap
  devServer: {
    disableHostCheck: true, // 忽略 Host 检查
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": resolve("src"), // 使用别名 @ 映射 src 目录
      },
    },
  },
};