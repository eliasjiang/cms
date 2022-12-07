const path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCssAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const buildPath = path.resolve(__dirname, "dist");

module.exports = {
  // This option controls if and how source maps are generated.
  // https://webpack.js.org/configuration/devtool/
  devtool: "source-map",

  // https://webpack.js.org/concepts/entry-points/#multi-page-application
  entry: {
    index: "./src/index.js",
    about: "./src/about.js",
    guestbook: "./src/guestbook.js",
    signin: "./src/signin.js",
    signup: "./src/signup.js",
    forgot: "./src/forgot.js",
    tools: "./src/tools.js",
    course: "./src/course.js",
    coursedetail: "./src/coursedetail.js",
    action: "./src/course.js",
    actiondetail: "./src/actiondetail.js",
    profile: "./src/profile.js",
    subscription: "./src/subscription.js",
    password: "./src/password.js",
    favorite: "./src/favorite.js",
    foodsearch: "./src/foodsearch.js",
    page: "./src/page.js",
    contact: "./src/contact.js",
  },

  // how to write the compiled files to disk
  // https://webpack.js.org/concepts/output/
  output: {
    filename: "[name].js",
    path: buildPath,
  },

  // https://webpack.js.org/concepts/loaders/
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "postcss-loader"],
      },
      {
        test: /\.(gif|png|jpe?g|svg)$/i,
        use: [
          "file-loader",
          {
            loader: "image-webpack-loader",
            options: {
              bypassOnDebug: true, // webpack@1.x
              disable: true, // webpack@2.x and newer
            },
          },
        ],
      },
    ],
  },

  // https://webpack.js.org/concepts/plugins/
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: "./src/index.html",
      inject: true,
      chunks: ["index"],
      filename: "index.html",
    }),
    new HtmlWebpackPlugin({
      template: "./src/about.html",
      inject: true,
      chunks: ["about"],
      filename: "about.html",
    }),
    new HtmlWebpackPlugin({
      template: "./src/guestbook.html",
      inject: true,
      chunks: ["guestbook"],
      filename: "guestbook.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/signin.html",
      inject: true,
      chunks: ["signin"],
      filename: "signin.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/signup.html",
      inject: true,
      chunks: ["signup"],
      filename: "signup.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/forgot.html",
      inject: true,
      chunks: ["forgot"],
      filename: "forgot.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/tools.html",
      inject: true,
      chunks: ["tools"],
      filename: "tools.html",
    }),
    new HtmlWebpackPlugin({
      template: "./src/foodsearch.html",
      inject: true,
      chunks: ["foodsearch"],
      filename: "foodsearch.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/action.html",
      inject: true,
      chunks: ["action"],
      filename: "action.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/actiondetail.html",
      inject: true,
      chunks: ["actiondetail"],
      filename: "actiondetail.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/course.html",
      inject: true,
      chunks: ["course"],
      filename: "course.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/coursedetail.html",
      inject: true,
      chunks: ["coursedetail"],
      filename: "coursedetail.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/profile.html",
      inject: true,
      chunks: ["profile"],
      filename: "profile.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/subscription.html",
      inject: true,
      chunks: ["subscription"],
      filename: "subscription.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/password.html",
      inject: true,
      chunks: ["password"],
      filename: "password.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/favorite.html",
      inject: true,
      chunks: ["favorite"],
      filename: "favorite.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/contact.html",
      inject: true,
      chunks: ["contact"],
      filename: "contact.html",
    }),
    new MiniCssExtractPlugin({
      filename: "[name].css",
      chunkFilename: "[id].css",
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          // 从public中复制文件
          from: path.resolve(__dirname, "public"),
          // 把复制的文件存放到dis里面
          to: path.resolve(__dirname, "dist"),
        },
      ],
    }),
  ],

  // https://webpack.js.org/configuration/optimization/
  optimization: {
    minimize: true,
    minimizer: [new OptimizeCssAssetsPlugin({})],
  },
};
