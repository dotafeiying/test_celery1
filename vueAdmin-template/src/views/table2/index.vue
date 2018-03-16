<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
      <el-form :inline="true" :model="filters" size="small">
        <el-form-item>
          <el-input v-model="filters.name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getUsers">查询</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleAdd">新增</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <el-table :data="users" size="mini" highlight-current-row v-loading="listLoading" @selection-change="selsChange" style="width: 100%;">
      <el-table-column type="selection" width="55">
      </el-table-column>
      <el-table-column type="index" width="60">
      </el-table-column>
      <!--<el-table-column v-for="(value,key) in users[0]" :prop="key" :label="key"  sortable min-width="80">-->
      <!--</el-table-column>-->
      <el-table-column prop="id" label="id" min-width="60" sortable>
      </el-table-column>
      <el-table-column prop="task_id" label="task_id" min-width="260" sortable>
      </el-table-column>
      <el-table-column prop="first" label="first" min-width="100"  sortable>
      </el-table-column>
      <el-table-column prop="second" label="second" min-width="100" sortable>
      </el-table-column>
      <el-table-column prop="log_date" label="log_date" min-width="200" sortable>
      </el-table-column>
      <el-table-column label="地址" min-width="220" sortable>
        <template slot-scope="scope">
          <a :href="scope.row.url" class="link-type" target="_blank">{{ scope.row.url }}</a>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button type="danger" size="mini" @click="handleDel(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--工具条-->
    <el-col :span="24" class="toolbar">
      <el-button type="danger" size="small" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button>
      <!--<el-pagination background layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">-->
      <!--</el-pagination>-->
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="page" :page-sizes="[10,20,30,50]" :page-size="limit" layout="total, sizes, prev, pager, next, jumper" :total="total" style="float:right;">
      </el-pagination>
    </el-col>

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
        <el-form-item label="任务id" prop="task_id">
          <el-input v-model="editForm.task_id" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="first">
          <el-input-number v-model="editForm.first" auto-complete="off"></el-input-number>
        </el-form-item>
        <el-form-item label="second">
          <el-input-number v-model="editForm.second" :min="0" :max="20000000"></el-input-number>
        </el-form-item>
        <el-form-item label="log_date">
          <el-date-picker type="datetime" placeholder="选择日期" v-model="editForm.log_date"></el-date-picker>
        </el-form-item>
        <el-form-item label="地址">
          <el-input type="textarea" v-model="editForm.url"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click.native="editFormVisible = false">取消</el-button>
        <el-button type="primary" @click.native="editSubmit" :loading="editLoading">提交</el-button>
      </div>
    </el-dialog>

    <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
        <el-form-item label="任务id" prop="task_id">
          <el-input v-model="addForm.task_id" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="first">
          <el-input-number v-model="addForm.first" auto-complete="off"></el-input-number>
        </el-form-item>
        <el-form-item label="second">
          <el-input-number v-model="addForm.second" :min="0" :max="20000000"></el-input-number>
        </el-form-item>
        <el-form-item label="log_date">
          <el-date-picker type="datetime" placeholder="选择日期" v-model="addForm.log_date"></el-date-picker>
        </el-form-item>
        <el-form-item label="地址">
          <el-input type="textarea" v-model="addForm.url"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click.native="addFormVisible = false">取消</el-button>
        <el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
      </div>
    </el-dialog>
  </section>
</template>

<script>
  // import util from '@/utils/util'
  // import NProgress from 'nprogress'
  import { getAddListPage, removeAdd, batchRemoveAdd, editAdd, addAdd } from '@/api/table2'

  export default {
    data() {
      return {
        filters: {
          name: ''
        },
        users: [],
        limit: 20,
        total: 0,
        page: 1,
        listLoading: false,
        sels: [], // 列表选中列

        editFormVisible: false, // 编辑界面是否显示
        editLoading: false,
        editFormRules: {
          name: [
            { required: true, message: '请输入姓名', trigger: 'blur' }
          ]
        },
        // 编辑界面数据
        editForm: {
          id: 0,
          task_id: '',
          first: -1,
          second: 0,
          log_date: '',
          url: ''
        },

        addFormVisible: false, // 新增界面是否显示
        addLoading: false,
        addFormRules: {
          name: [
            { required: true, message: '请输入姓名', trigger: 'blur' }
          ]
        },
        // 新增界面数据
        addForm: {
          id: 0,
          task_id: '',
          first: -1,
          second: 0,
          log_date: '',
          url: ''
        }

      }
    },
    methods: {
      // 性别显示转换
      formatSex: function(row, column) {
        return row.sex === 1 ? '男' : row.sex === 0 ? '女' : '未知'
      },
      handleCurrentChange(val) {
        this.page = val
        this.getUsers()
      },
      handleSizeChange(val) {
        this.limit = val
        this.getUsers()
      },
      // 获取用户列表
      getUsers() {
        let para = {
          limit: this.limit,
          offset: (this.page - 1) * 20
          // name: this.filters.name
        }
        this.listLoading = true
        // NProgress.start();
        getAddListPage(para).then((res) => {
          console.log(res)
          this.total = res.count;
          this.users = res.results;
          this.listLoading = false;
          // NProgress.done();
        })
      },
      // 删除
      handleDel: function(index, row) {
        this.$confirm('确认删除该记录吗?', '提示', {
          type: 'warning'
        }).then(() => {
          this.listLoading = true;
          // NProgress.start();
          let para = { id: row.id };
          removeAdd(para).then((res) => {
            this.listLoading = false;
            // NProgress.done();
            this.$message({
              message: '删除成功',
              type: 'success'
            });
            this.getUsers();
          });
        }).catch(() => {

        });
      },
      // 显示编辑界面
      handleEdit: function(index, row) {
        this.editFormVisible = true;
        this.editForm = Object.assign({}, row);
      },
      // 显示新增界面
      handleAdd: function() {
        this.addFormVisible = true;
        this.addForm = {
          id: 0,
          task_id: '',
          first: 0,
          second: 0,
          log_date: '',
          url: ''
        };
      },
      // 编辑
      editSubmit: function() {
        this.$refs.editForm.validate((valid) => {
          if (valid) {
            this.$confirm('确认提交吗？', '提示', {}).then(() => {
              this.editLoading = true;
              // NProgress.start();
              let para = Object.assign({}, this.editForm);
              // para.log_date = (!para.log_date || para.log_date === '') ? '' : util.formatDate.format(new Date(para.log_date), 'yyyy-MM-dd');
              console.log(para)
              editAdd(para).then((res) => {
                this.editLoading = false;
                // NProgress.done();
                this.$message({
                  message: '提交成功',
                  type: 'success'
                });
                this.$refs['editForm'].resetFields();
                this.editFormVisible = false;
                this.getUsers();
              });
            });
          }
        });
      },
      // 新增
      addSubmit: function() {
        this.$refs.addForm.validate((valid) => {
          if (valid) {
            this.$confirm('确认提交吗？', '提示', {}).then(() => {
              this.addLoading = true;
              // NProgress.start();
              let para = Object.assign({}, this.addForm);
              // para.birth = (!para.birth || para.birth === '') ? '' : util.formatDate.format(new Date(para.birth), 'yyyy-MM-dd');
              addAdd(para).then((res) => {
                this.addLoading = false;
                // NProgress.done();
                this.$message({
                  message: '提交成功',
                  type: 'success'
                });
                this.$refs['addForm'].resetFields();
                this.addFormVisible = false;
                this.getUsers();
              });
            });
          }
        });
      },
      selsChange: function(sels) {
        this.sels = sels;
      },
      // 批量删除
      batchRemove: function() {
        var ids = this.sels.map(item => item.id).toString();
        this.$confirm('确认删除选中记录吗？', '提示', {
          type: 'warning'
        }).then(() => {
          this.listLoading = true;
          // NProgress.start();
          let para = { ids: ids };
          batchRemoveAdd(para).then((res) => {
            this.listLoading = false;
            // NProgress.done();
            this.$message({
              message: '删除成功',
              type: 'success'
            });
            this.getUsers();
          });
        }).catch(() => {

        });
      }
    },
    mounted() {
      this.getUsers();
    }
  }

</script>

<!--<style scoped>-->
<style lang="scss">

  .el-submenu [class^=fa] {
    vertical-align: baseline;
    margin-right: 10px;
  }

  .el-menu-item [class^=fa] {
    vertical-align: baseline;
    margin-right: 10px;
  }

  .toolbar {
    background: #f2f2f2;
    padding: 10px;
    /*// border:1px solid #dfe6ec;*/
    margin: 10px 0px;
    .el-form-item {
      margin-bottom: 10px;
    }
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: all .2s ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0;
  }

  .link-type,
  .link-type:focus {
    color: #337ab7;
    cursor: pointer;
    &:hover {
      color: rgb(32, 160, 255);
    }
  }
</style>
