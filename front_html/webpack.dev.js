const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
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
    favorite: "./src/favorite.js",
    password: "./src/password.js",
    foodsearch: "./src/foodsearch.js",
    page: "./src/page.js",
    contact: "./src/contact.js",
  },

  // https://webpack.js.org/configuration/dev-server/
  devServer: {
    contentBase: [
      path.resolve(__dirname, "public"),
      path.resolve(__dirname, "dist"),
    ],
    port: 8080,
  },

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader", "postcss-loader"],
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
      template: "./src/profile.html",
      inject: true,
      chunks: ["profile"],
      filename: "profile.html",
    }),

    new HtmlWebpackPlugin({
      template: "./src/contact.html",
      inject: true,
      chunks: ["contact"],
      filename: "contact.html",
    }),
  ],
};
