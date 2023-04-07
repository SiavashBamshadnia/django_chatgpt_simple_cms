addEventListener('load', function () {
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    const generateTitleFromContentButton = document.querySelector('#generate-title-from-content')
    const generateSummaryFromContentButton = document.querySelector('#generate-summary-from-content')
    const generateContentFromTitleButton = document.querySelector('#generate-content-from-title')
    const generateContentFromSummaryButton = document.querySelector('#generate-content-from-summary')

    /**
     * Generates a title from the content of a post.
     */
    generateTitleFromContentButton.onclick = async function (click) {
        click.preventDefault()

        const content = document.querySelector('textarea[name=content]').value

        if (!content) {
            alert('Please fill out content field.')
            return
        }

        generateTitleFromContentButton.disabled = true
        try {
            const response = await axios.post('/api/posts/generate_title_from_content/', {'content': content}, {
                headers: {'X-CSRFToken': csrf_token}
            })
            document.querySelector('input[name=title]').value = response.data
        } catch (error) {
            console.log(error)
        }
        generateTitleFromContentButton.disabled = false
    }

    /**
     * Generates a summary from the content of a post.
     */
    generateSummaryFromContentButton.onclick = async function (click) {
        click.preventDefault()

        const content = document.querySelector('textarea[name=content]').value

        if (!content) {
            alert('Please fill out content field.')
            return
        }

        generateSummaryFromContentButton.disabled = true
        try {
            const response = await axios.post('/api/posts/generate_summary_from_content/', {'content': content}, {
                headers: {'X-CSRFToken': csrf_token}
            })
            document.querySelector('textarea[name=summary]').value = response.data
        } catch (error) {
            console.log(error)
        }
        generateSummaryFromContentButton.disabled = false
    }

    /**
     * Generates the content of a post from its title.
     */
    generateContentFromTitleButton.onclick = async function (click) {
        click.preventDefault()

        const title = document.querySelector('input[name=title]').value

        if (!title) {
            alert('Please fill out title field.')
            return
        }

        generateContentFromTitleButton.disabled = true
        try {
            const response = await axios.post('/api/posts/generate_content_from_title/', {'title': title}, {
                headers: {'X-CSRFToken': csrf_token}
            })
            document.querySelector('textarea[name=content]').value = response.data
        } catch (error) {
            console.log(error)
        }
        generateContentFromTitleButton.disabled = false
    }

    /**
     * Generates a summary of a post from its content.
     */
    generateContentFromSummaryButton.onclick = async function (click) {
        click.preventDefault()

        const summary = document.querySelector('textarea[name=summary]').value

        if (!summary) {
            alert('Please fill out summary field.')
            return
        }

        generateContentFromSummaryButton.disabled = true
        try {
            const response = await axios.post('/api/posts/generate_content_from_summary/', {'summary': summary}, {
                headers: {'X-CSRFToken': csrf_token}
            })
            document.querySelector('textarea[name=content]').value = response.data
        } catch (error) {
            console.log(error)
        }
        generateContentFromSummaryButton.disabled = false
    }
})
