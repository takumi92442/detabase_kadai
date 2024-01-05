import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Title from './title'
import {List} from './list'
import Footer from './footer'

function header(){
  return(
    <>
    <Title />
    <div className='list'>
    <List  />
    </div>
    <Footer />
    </>

  )
}



export default header