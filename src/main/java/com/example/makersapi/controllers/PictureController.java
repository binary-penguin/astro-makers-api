package com.example.makersapi.controllers;

import com.example.makersapi.domain.Picture;
import com.example.makersapi.repositories.PictureRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class PictureController {
    private final PictureRepository pictureRepository;

    public PictureController(PictureRepository pictureRepository) {
        this.pictureRepository = pictureRepository;
    }

    @CrossOrigin
    @GetMapping("/pictures/{start}")
    public Page<Picture> getPictures(@PathVariable int start) {
        Pageable range = PageRequest.of(start, 10);
        return pictureRepository.findAll(range);
    }

    @CrossOrigin
    @GetMapping("/pictures2")
    public List<Picture> getPictures2() {
        return pictureRepository.findAll();
    }
}
