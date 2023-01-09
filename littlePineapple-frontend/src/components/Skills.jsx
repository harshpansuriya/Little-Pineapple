export default function Skills(props) {

    const displaySkills = (props) => {
        const {skills} = props

        if (skills.length > 0 ){
            return(
                skills.map((skill, index) => {
                    console.log(skill)

                    return(
                        <div key = {skill.id}>
                            <h3>{skill.first_name}</h3>
                            <p>Special Skill is {skill.special_skill}</p>
                        </div>
                    )
                })
            )
        } else {
            return (
                <h3>No skills yet!</h3>
            )
        }
    }

    return(
        <>
            {displaySkills(props)}
        </>
    )
}