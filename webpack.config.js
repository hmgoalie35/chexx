const path = require('path');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

// Paths
const projectDir = path.resolve(__dirname);
const frontendDir = path.join(projectDir, 'frontend');
const staticDir = path.join(frontendDir, 'static');
const jsDir = path.join(staticDir, 'js');
const scssDir = path.join(staticDir, 'scss');
const fontsDir = path.join(staticDir, 'fonts');
const buildDir = path.join(staticDir, 'build');
const staticUrl = '/static/';
const publicPath = `${staticUrl}${path.basename(buildDir)}/`;

module.exports = function (env, argv) {
  const { mode } = argv;
  const isProduction = mode === 'production';
  const fileName = '[name]';
  const entry = `${jsDir}/main.js`;

  return {
    mode,
    entry,
    output: {
      filename: `js/${fileName}.js`,
      chunkFilename: `js/${fileName}.js`,
      path: buildDir,
      library: 'App',
      publicPath,
    },
    module: {
      rules: [
        {
          test: /\.scss$/,
          include: [scssDir],
          use: [
            MiniCssExtractPlugin.loader,
            {
              loader: 'css-loader'
            },
            {
              loader: 'sass-loader'
            }
          ]
        },
        {
          test: /\.(png|svg|jpe?g|gif)(\?v=\d+\.\d+\.\d+)?$/,
          loader: 'file-loader',
          options: {
            outputPath: 'img/'
          }
        },
        {
          test: /\.(woff|woff2|eot|ttf|otf)(\?v=\d+\.\d+\.\d+)?$/,
          include: [fontsDir],
          loader: 'file-loader',
          options: {
            outputPath: 'fonts/'
          }
        }
      ],
    },
    watch: !isProduction,
    plugins: [
      new CleanWebpackPlugin(),
      new MiniCssExtractPlugin({
        filename: `css/${fileName}.css`
      }),
    ]
  };
};
