import request from '@/utils/request'
import $ from 'jquery'

const base = ''

export function getList1(params) {
  return request({
    url: '/add/',
    method: 'get',
    params
  })
}

// export const getUserList = params => { return request.get(`${base}/user/list`, { params: params }) }

export const getAddListPage = params => { return request.get(`${base}/add/`, { params: params }) }

// export const removeAdd = params => { return request.get(`${base}/add/remove`, { params: params }) }
export const removeAdd = params => { return request.delete(`${base}/add/${params.id}/`) }

export const batchRemoveAdd = params => { return request.get(`${base}/add/batchremove`, { params: params }) }

// export const editAdd = params => { return request.put(`${base}/add/${params.id}/`, params) }
export const editAdd = params => {
  return request({
    url: `${base}/add/${params.id}/`,
    method: 'put',
    transformRequest: [function(data) {
      // Do whatever you want to transform the data
      let ret = ''
      for (let it in data) {
        ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
      }
      return ret
    }],
    data: params
  })
}

export const addAdd = params => { return request.post(`${base}/add/`, $.param(params)) }
// export const addAdd = params => {
//   // let { id,url,...d } = params;
//   // let d = {task_id:'11111',first:1,second:1,log_date:''}
//   return request({
//     url: `${base}/add/`,
//     method: 'post',
//     transformRequest: [function(data) {
//       let ret = ''
//       for (let it in data) {
//         ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
//       }
//       console.log(ret)
//       return ret
//     }],
//     data: params
//   })
// }
