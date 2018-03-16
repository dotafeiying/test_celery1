import request from '@/utils/request'

export function getList1(params) {
  return request({
    url: '/table1/',
    method: 'get',
    params
  })
}
