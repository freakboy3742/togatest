var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
// var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  context: __dirname,
  entry: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      './assets/js/togatest.js'
  ],

  output: {
      path: path.resolve('./assets/bundles/'),
      //   filename: "[name]-[hash].js",
      filename: "[name].js",
      // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
      publicPath: 'http://localhost:3000/assets/bundles/',
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack.stats.json'})
  ],

  module: {
    loaders: [
            {
                test: /\.js$/,
                loader: "babel",
                exclude: /node_modules/
            },
            {
                include: /\.json$/,
                loader: "json"
            },
            {
                test: /\.css$/,
                // loader: ExtractTextPlugin.extract('style', 'css', 'resolve-url')
                loaders: ['style', 'css']
            },
            {
                test: /\.s?css$/,
                // loader: ExtractTextPlugin.extract('style', 'css', 'sass', 'resolve-url')
                loaders: ['style', 'css', 'sass']
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'url?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'file'
            }
    ]
  }
}
