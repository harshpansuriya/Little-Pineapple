import axios from "axios";
import {useEffect, useState} from "react";
import Skills from "./components/Skills.jsx";

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
        <Skills skills = {skills} />
    )
}