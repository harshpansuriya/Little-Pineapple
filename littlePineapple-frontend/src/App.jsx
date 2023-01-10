import axios from "axios";
import {useEffect, useState} from "react";
import Skills from "./components/Skills.jsx";
import Header from "./components/Header.jsx";
import Main from "./components/Main.jsx";

export default function App() {

    const [skills, getSkills] = useState('')

    const url = 'http://localhost:8000/api/skills/'

    useEffect(() => {
        getAllSkills()
    }, [])

    const getAllSkills = () => {
        axios.get(url)
            .then((response) => {
                const allSkills = response.data
                getSkills(allSkills)
            })
            .catch(error => console.log(`Error: ${error}`))
    }
    return(
        <>
            <Header />
            <Main />
            <Skills skills = {skills} />
        </>
    )
}