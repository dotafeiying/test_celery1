// eslint-disable-next-line
/* eslint-disable */

<template>
  <div class="home">
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-table :data="bookList" style="width: 100%" border>
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="编号">
                  <span>{{ props.row.id }}</span>
                </el-form-item>
                <el-form-item label="所属店铺">
                  <span>{{ props.row.first }}</span>
                </el-form-item>
                <el-form-item label="商品 ID">
                  <span>{{ props.row.second }}</span>
                </el-form-item>

              </el-form>
            </template>
          </el-table-column>
          <el-table-column prop="id" label="编号" min-width="100">
            <template slot-scope="scope"> {{ scope.row.id }} </template>
          </el-table-column>
          <el-table-column prop="first" label="书名" min-width="100">
            <template slot-scope="scope"> {{ scope.row.first }} </template>
          </el-table-column>
          <el-table-column prop="second" label="添加时间" min-width="100">
            <template slot-scope="scope"> {{ scope.row.second }} </template>
          </el-table-column>
          <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="deleteRow(scope.$index, bookList)"
                type="text"
                size="small">
                移除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      bookList: []
    }
  },
  mounted: function () {
    this.showBooks()
  },
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    // addBook(){
    //   this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
    //     .then((response) => {
    //         var res = JSON.parse(response.bodyText)
    //         if (res.error_num == 0) {
    //           this.showBooks()
    //         } else {
    //           this.$message.error('新增书籍失败，请重试')
    //           console.log(res['msg'])
    //         }
    //     })
    // },
    showBooks () {
      this.$http.get('http://127.0.0.1:5000/api/add/')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          this.bookList = res
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 30%;
  }
</style>
