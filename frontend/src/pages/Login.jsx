import React from 'react'

export default function Login() {
  return (
    <div className='flex justify-center'>
      

<form className='w-[40%] bg-white p-4 rounded-xl'>
  <h3 className='text-2xl my-4 font-bold font-mono'>Login</h3>
  <div class="relative mb-6">
  <label class="flex  items-center mb-2 text-gray-600 text-sm font-medium">Username <svg width="7" height="7" class="ml-1" viewBox="0 0 7 7" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M3.11222 6.04545L3.20668 3.94744L1.43679 5.08594L0.894886 4.14134L2.77415 3.18182L0.894886 2.2223L1.43679 1.2777L3.20668 2.41619L3.11222 0.318182H4.19105L4.09659 2.41619L5.86648 1.2777L6.40838 2.2223L4.52912 3.18182L6.40838 4.14134L5.86648 5.08594L4.09659 3.94744L4.19105 6.04545H3.11222Z" fill="#EF4444" />
    </svg>
  </label>
  <input type="text"  class="block w-full h-11 px-5 py-2.5 bg-white leading-7 text-base font-normal shadow-xs text-gray-900 bg-transparent border border-gray-300 rounded-full placeholder-gray-400 focus:outline-none " placeholder="" required=""/>
  </div>
  <div class="relative mb-6">
  <label class="flex  items-center mb-2 text-gray-600 text-sm font-medium">Password <svg width="7" height="7" class="ml-1" viewBox="0 0 7 7" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M3.11222 6.04545L3.20668 3.94744L1.43679 5.08594L0.894886 4.14134L2.77415 3.18182L0.894886 2.2223L1.43679 1.2777L3.20668 2.41619L3.11222 0.318182H4.19105L4.09659 2.41619L5.86648 1.2777L6.40838 2.2223L4.52912 3.18182L6.40838 4.14134L5.86648 5.08594L4.09659 3.94744L4.19105 6.04545H3.11222Z" fill="#EF4444" />
    </svg>
  </label>
  <input type="text" class="block w-full h-11 px-5 py-2.5 bg-white leading-7 text-base font-normal shadow-xs text-gray-900 bg-transparent border border-gray-300 rounded-full placeholder-gray-400 focus:outline-none " placeholder="" required=""/>
  
  </div>
  <button class="w-full h-12 bg-orange-600 hover:bg-orange-800 transition-all duration-700 rounded-full shadow-xs text-white text-base font-semibold leading-6 mb-6">Sign in</button>
</form>


    </div>
  )
}
