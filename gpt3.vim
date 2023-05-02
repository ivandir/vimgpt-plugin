function! CallGPT3(prompt)
  let l:escaped_prompt = shellescape(a:prompt)
  let l:response = system("python gpt3.py " . l:escaped_prompt)

  if v:shell_error != 0
    echohl ErrorMsg
    echo "Error calling GPT-3:"
    echo l:response
    echohl None
    return
  endif

  tabnew
  call setline(1, split(l:response, "\n"))
  normal gg
endfunction

command! -nargs=1 -complete=file GPT3 call CallGPT3(<q-args>)
